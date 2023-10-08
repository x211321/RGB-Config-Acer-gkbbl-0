import os
import wx
import time
import shutil
import subprocess
import threading
import zipfile
import urllib.request

import lib.ui as ui
import lib.var as var

import gettext
_ = gettext.gettext

####################
# class AcerRGBGUI_Install_Module
#-------------------
# Extend wx wxPython About dialog
class AcerRGBGUI_Install_Module(ui.dialog_install_module):
    def __init__(self, parent):
        ui.dialog_install_module.__init__(self, parent)
        self.preferences = parent.preferences
        self.log = []


    #########################################
    ## Event handler
    #########################################


    ####################
    # on_install
    #-------------------
    # Event handler - install button
    def on_install(self, event):
        self.initLabels()

        self.warnings   = []
        self.errors     = []
        self.initSystem = ""

        self.button_install_module_start.Disable()
        self.button_install_module_exit.Disable()

        self.thread = threading.Thread(target=self.installThread)
        self.thread.start()


    ####################
    # on_exit
    #-------------------
    # Event handler - exit button
    def on_exit(self, event):
        self.Destroy() 


    ####################
    # on_show
    #-------------------
    # Event handler - show
    def on_show(self, event):
        self.initLabels()
        self.Center()


    ####################
    # on_close
    #-------------------
    # Event handler - close
    def on_close(self, event):
        if not self.thread.is_alive():
            self.Destroy()




    #########################################
    ## Dialog interaction
    #########################################


    ####################
    # installLog
    #-------------------
    # Installation thread
    def installLog(self, message):
        print(message)
        self.log.append(message)


    ####################
    # installThread
    #-------------------
    # Installation thread
    def installThread(self):

        try:
            self.installLog(_("\n\nBeginning installation process"))
            self.installLog(_("------------------------------\n"))

            # Step 1 - Check system requirements
            self.installLog(_("\n\nStep 1 - Check system requirements"))
            self.installLog(_("------------------------------\n"))

            self.checkManufacturer()
            self.checkModel()
            self.checkSecureBoot()
            self.checkInitSystem()

            if not self.checkResult():
                self.button_install_module_start.Enable()
                return
            
            # Step 2 - Download installation files
            self.installLog(_("\n\nStep 2 - Download installation files"))
            self.installLog(_("------------------------------\n"))

            if not self.downloadFiles():
                dlg = wx.MessageDialog(self, _("Installation files could not be downloaded.\n\nInstallation aborted.")
                                            , _("Download failed"), wx.OK)
                dlg.Center()
                dlg.ShowModal()
                return
            
            # Step 3 - Extract installation files
            self.installLog(_("\n\nStep 3 - Extract installation files"))
            self.installLog(_("------------------------------\n"))

            if not self.extractFiles():
                dlg = wx.MessageDialog(self, _("Installation files could not be extracted.\n\nInstallation aborted.")
                                            , _("Extract failed"), wx.OK)
                dlg.Center()
                dlg.ShowModal()
                return
            
            # Step 4 - Install installation files
            self.installLog(_("\n\nStep 4 - Install installation files"))
            self.installLog(_("------------------------------\n"))

            if not self.installFiles():
                dlg = wx.MessageDialog(self, _("The install script could not be executed.\n\nInstallation aborted.")
                                            , _("Install failed"), wx.OK)
                dlg.Center()
                dlg.ShowModal()
                return
            
            # Step 5 - Verify installation
            self.installLog(_("\n\nStep 5 - Verify installation"))
            self.installLog(_("------------------------------\n"))

            if not self.verifyInstallation():
                dlg = wx.MessageDialog(self, _("One or more RGB devices unavailable.\n\n" \
                                               "Either the installation has failed or the kernel module could not be loaded.\n\n" \
                                               "Sometime the kernel module cannot be loaded until the device was restarted.")
                                            , _("Verification failed"), wx.OK)
                dlg.Center()
                dlg.ShowModal()

        except:
            if self.preferences["debug"]:
                raise

        finally:
            self.button_install_module_start.Enable()
            self.button_install_module_exit.Enable()


    ####################
    # updateLabel
    #-------------------
    # Update label
    def updateLabel(self, label, text, color):
        label.SetLabelText(_(text))
        label.SetForegroundColour(color)
        self.Layout()


    ####################
    # runCommandSudo
    #-------------------
    # Run a command with sudo privileges
    def runCommandSudo(self, command, shell=False, cwd=None, noLog=False):
        self.installLog("Command sudo: " + command)

        sudo   = "sudo "
        sudo_s = "sudo -S "

        if not shell:
            sudo    = sudo.split()
            sudo_s  = sudo_s.split()
            command = command.split()

        # Check if sudo password required
        p = subprocess.run(["sudo", "-vn"])

        if not p.returncode == 0:
            dlg = wx.PasswordEntryDialog(self, _("Authentication required.\n\n" \
                                                 "RGB Config (acer-gkbbl-0) must perform an action that requires\nroot privileges."), 
                                                 caption=_("Authentication required"))
            
            dlg.ShowModal()
            
            p1 = subprocess.Popen(["echo",dlg.GetValue()], stdout=subprocess.PIPE)
            p2 = subprocess.Popen(sudo_s + command, stdin=p1.stdout, stdout=subprocess.PIPE, shell=shell, cwd=cwd)
        else:
            p2 = subprocess.Popen(sudo + command, stdout=subprocess.PIPE, shell=shell, cwd=cwd)

        result = p2.stdout.read().decode()

        if not noLog and len(result):
            self.installLog("\nOutput: " + result)

        return result
    

    ####################
    # runCommand
    #-------------------
    # Run a command
    def runCommand(self, command, shell=False, cwd=None, noLog=False):
        self.installLog("Command: " + command)

        if not shell:
            command = command.split()

        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=shell, cwd=cwd)

        result = p.stdout.read().decode()

        if not noLog and len(result):
            self.installLog("\nOutput: " + result)

        return result


    ####################
    # checkManufacturer
    #-------------------
    # Retrieve manufacturer information
    def checkManufacturer(self):
        label = self.label_install_module_step1_system_requirements_manufacturer_result
        color = var.YELLOW

        try:
            manufacturer = self.runCommandSudo("dmidecode -s system-manufacturer", shell=True).strip()

            if manufacturer.lower().find("acer") > -1:
                color = var.GREEN
            else:
                self.warnings.append(_("Manufacturers other than Acer are most likely not compatible with this module"))
        except:
            if self.preferences["debug"]:
                raise
            manufacturer = _("Unknown")
            self.warnings.append(_("The device manufacturer could not be detected"))

        self.updateLabel(label, manufacturer, color)


    ####################
    # checkModel
    #-------------------
    # Retrieve model information
    def checkModel(self):
        label = self.label_install_module_step1_system_requirements_model_result
        color = var.YELLOW

        device_supported  = False
        supported_devices = []

        try:
            model = self.runCommandSudo("dmidecode -s system-product-name", shell=True).strip()

            # Check if model is on list of already known devices
            # If not, we will try to check the readme file of the modules github page
            for supported_device in var.SUPPORTED_DEVICES:
                if supported_device.lower() in model.lower():
                    device_supported = True
                    break

            if not device_supported and not self.preferences["debug"]:
                try:
                    # Extract compatibility list from github readme
                    contents = urllib.request.urlopen(var.MODULE_WEBSITE).read().decode()

                    start = "<th>Product name</th>"
                    end   = "</table>"

                    contents = contents[contents.find(start)+len(start):contents.rfind(end)]

                    start  = "<tr>\n<td>"
                    end    = "</td>"
                    index  = 0

                    while index > -1:
                        index = contents.find(start, index)

                        if index > -1:
                            index += len(start)
                            supported_devices.append(contents[index:contents.find(end, index)])

                    # Check if model is in list of supported devices
                    for supported_device in supported_devices:
                        if supported_device.lower() in model.lower():
                            device_supported = True
                            break

                except:
                    if self.preferences["debug"]:
                        raise
                    self.warnings.append(_("The compatibility list could not be retrieved"))

        except:
            if self.preferences["debug"]:
                raise
            model = _("Unknown")
            self.warnings.append(_("The device model could not be detected"))

        if device_supported:
            color = var.GREEN
        else:
            color = var.YELLOW
            self.warnings.append(_("The model number does not appear on the list of supported devices"))

        self.updateLabel(label, model, color)


    ####################
    # checkSecureBoot
    #-------------------
    # Retrieve secure boot information
    def checkSecureBoot(self):
        label = self.label_install_module_step1_system_requirements_secureboot_result

        try:
            result = self.runCommand("od --address-radix=n --format=u1 /sys/firmware/efi/efivars/SecureBoot-*", True).strip()

            secure_boot_enabled = int(result[-1])

            if not secure_boot_enabled:
                self.updateLabel(label, _("Disabled"), var.GREEN)
            else:
                self.updateLabel(label, _("Enabled"), var.RED)
                self.errors.append(_("Secure boot should be disabled. The module will probably not work with secure boot enabled"))

        except:
            if self.preferences["debug"]:
                raise
            self.updateLabel(label, _("Unknown"), var.YELLOW)
            self.warnings.append(_("Secure boot state could not be detected"))

    
    ####################
    # checkInitSystem
    #-------------------
    # Retrieve the active init system
    def checkInitSystem(self):
        label = self.label_install_module_step1_system_requirements_initsystem_result
        color = var.YELLOW

        init_found = False
        
        try:
            # Check /sbin/init symlink
            if not init_found:
                init_symlink = self.runCommand("readlink -f /sbin/init", True).lower()

                if not init_found and "systemd" in init_symlink:
                    self.initSystem = var.MODULE_INITSYSTEM_SYSTEMD
                    color = var.GREEN
                    init_found = True

                if not init_found and "sysvinit" in init_symlink:
                    self.initSystem = var.MODULE_INITSYSTEM_SYSVINIT
                    color = var.YELLOW
                    init_found = True
                    self.warnings.append(_("The init system seems to be unsupported"))
                    self.warnings.append(_("No service will be installed, the module will only work until shutdown"))

                if not init_found and "openrc" in init_symlink:
                    self.initSystem = var.MODULE_INITSYSTEM_OPENRC
                    color = var.GREEN
                    init_found = True

            # Check /sbin/init strings
            if not init_found:
                init_strings = self.runCommand("strings /sbin/init", True, noLog=True).lower()

                if not init_found and "systemd" in init_strings:
                    self.initSystem = var.MODULE_INITSYSTEM_SYSTEMD
                    color = var.GREEN
                    init_found = True

                if not init_found and "sysvinit" in init_strings:
                    self.initSystem = var.MODULE_INITSYSTEM_SYSVINIT
                    color = var.YELLOW
                    init_found = True
                    self.warnings.append(_("The init system seems to be unsupported"))
                    self.warnings.append(_("No service will be installed, the module will only work until shutdown"))

                if not init_found and "openrc" in init_strings:
                    self.initSystem = var.MODULE_INITSYSTEM_OPENRC
                    color = var.GREEN
                    init_found = True
        except:
            if self.preferences["debug"]:
                raise
            self.initSystem = _("Unknown")
            color = var.YELLOW
            self.warnings.append(_("The init system could not be detected"))
            self.warnings.append(_("No service will be installed, the module will only work until shutdown"))

        self.updateLabel(label, self.initSystem, color)


    ####################
    # checkResult
    #-------------------
    # Evaluate the result of the system requirement checks
    def checkResult(self):
        if len(self.warnings) or len(self.errors):
            error_info = _("System might not meet all requirements.\n")

            if len(self.warnings):
                error_info += _("\nWarnings\n---------\n")

                for entry in self.warnings:
                    error_info += " - " + entry + "\n"

            if len(self.errors):
                error_info += _("\nPotential errors\n---------\n")

                for entry in self.errors:
                    error_info += " - " + entry + "\n"

            error_info += _("\nYou can still try to continue the installation but the module might not work with your setup.")

            dlg = wx.MessageDialog(self, _(error_info)
                                    , _("System check"), wx.YES_NO)
            res = dlg.ShowModal()

            if res == wx.ID_YES:
                return True
            else:
                return False
        else:
            return True


    ####################
    # downloadFiles
    #-------------------
    # Download the installation files
    def downloadFiles(self):
        label = self.label_install_module_step2_download_state

        self.updateLabel(label, _("Downloading..."), var.BLUE)

        # Remove old file
        if not self.preferences["debug"]:
            self.installLog(_("Removing old file: ") + var.MODULE_DOWNLOAD_PATH)
            if os.path.exists(var.MODULE_DOWNLOAD_PATH):
                os.remove(var.MODULE_DOWNLOAD_PATH)

        # Download source code archive
        try:
            if not self.preferences["debug"]:
                self.installLog(_("Downloading installation file: ") + var.MODULE_DOWNLOAD)
                urllib.request.urlretrieve(var.MODULE_DOWNLOAD, var.MODULE_DOWNLOAD_PATH)

            # Check if download successful
            if os.path.exists(var.MODULE_DOWNLOAD_PATH):
                self.installLog(_("Download successful file: ") + var.MODULE_DOWNLOAD_PATH)
                self.updateLabel(label, _("Success"), var.GREEN)
                return True
            else:
                self.installLog(_("Download failed"))
                self.updateLabel(label, _("Failed"), var.RED)
                return False
        except:
            if self.preferences["debug"]:
                raise
            self.installLog(_("Download failed"))
            self.updateLabel(label, _("Failed"), var.RED)
            return False


    ####################
    # extractFiles
    #-------------------
    # Extract the installation files
    def extractFiles(self):
        label = self.label_install_module_step3_extract_result
        self.updateLabel(label, _("Extracting..."), var.BLUE)

        try:
            if os.path.exists(var.MODULE_EXTRACT_PATH):
                self.installLog(_("Removing old installation files: ") + var.MODULE_EXTRACT_PATH)
                shutil.rmtree(var.MODULE_EXTRACT_PATH)

            self.installLog(_("Extracting installation files: ") + var.MODULE_DOWNLOAD_PATH)
            with zipfile.ZipFile(var.MODULE_DOWNLOAD_PATH, 'r') as zip:
                zip.extractall(var.MODULE_EXTRACT_PATH)

            if os.path.exists(var.MODULE_EXTRACT_PATH):
                self.installLog(_("Installation files extracted to: ") + var.MODULE_EXTRACT_PATH)
                self.updateLabel(label, _("Success"), var.GREEN)
                return True
            else:
                self.installLog(_("Extract failed"))
                self.updateLabel(label, _("Failed"), var.RED)
                return False

        except:
            if self.preferences["debug"]:
                raise
            self.installLog(_("Extract failed"))
            self.updateLabel(label, _("Failed"), var.RED)
            return False
        

    ####################
    # installFiles
    #-------------------
    # Install the installation files
    def installFiles(self):
        label = self.label_install_module_step4_install_result
        self.updateLabel(label, _("Installing..."), var.BLUE)

        try:
            dirs = os.listdir(var.MODULE_EXTRACT_PATH)

            if self.initSystem == var.MODULE_INITSYSTEM_SYSTEMD:
                installFile = var.MODULE_INSTALL_SYSTEMD
            elif self.initSystem == var.MODULE_INITSYSTEM_OPENRC:
                installFile = var.MODULE_INSTALL_OPENRC
            else:
                installFile = var.MODULE_INSTALL_NOSERVICE

            path = os.path.join(var.MODULE_EXTRACT_PATH, dirs[0])
            install   = os.path.join(path, installFile)

            self.installLog(_("Setting execute permissions on install files"))
            self.runCommand("chmod +x " + os.path.join(path, "*.sh"), True)

            self.installLog(_("Running install script: ") + install)
            output = self.runCommandSudo(install, shell=True, cwd=path)
            self.installLog(output)

            for i in range(30):
                if os.path.exists("/opt/turbo-fan/src/facer.ko"):
                    break
                else:
                    time.sleep(1)
            
            if os.path.exists("/opt/turbo-fan/src/facer.ko"):
                self.installLog(_("Install successful: ") + "/opt/turbo-fan/")
                self.updateLabel(label, _("Success"), var.GREEN)
                return True
            else:
                self.installLog(_("Install failed"))
                self.updateLabel(label, _("Failed"), var.RED)
                return False

        except:
            if self.preferences["debug"]:
                raise
            self.installLog(_("Install failed"))
            self.updateLabel(label, _("Failed"), var.RED)
            return False


    ####################
    # verifyInstallation
    #-------------------
    # Verify installation
    def verifyInstallation(self):
        allAvailable = True

        if os.path.exists(var.RGB_DEVICE):
            self.updateLabel(self.label_install_module_step5_verify_rgb_result, _("Available"), var.GREEN)
        else:
            self.updateLabel(self.label_install_module_step5_verify_rgb_result, _("Unavailable"), var.RED)
            allAvailable = False

        if os.path.exists(var.RGB_DEVICE_STATIC):
            self.updateLabel(self.label_install_module_step5_verify_rgbstatic_result, _("Available"), var.GREEN)
        else:
            self.updateLabel(self.label_install_module_step5_verify_rgbstatic_result, _("Unavailable"), var.RED)
            allAvailable = False

        return allAvailable


    ####################
    # initLabels
    #-------------------
    # Initialize the dialog labels
    def initLabels(self):
        self.label_install_module_step1_system_requirements_result.SetLabelText("")
        self.label_install_module_step1_system_requirements_manufacturer_result.SetLabelText("")
        self.label_install_module_step1_system_requirements_model_result.SetLabelText("")
        self.label_install_module_step1_system_requirements_secureboot_result.SetLabelText("")
        self.label_install_module_step1_system_requirements_initsystem_result.SetLabelText("")
        self.label_install_module_step2_download_result.SetLabelText("")
        self.label_install_module_step2_download_state.SetLabelText("")
        self.label_install_module_step3_extract_result.SetLabelText("")
        self.label_install_module_step4_install_result.SetLabelText("")
        self.label_install_module_step5_verify_result.SetLabelText("")
        self.label_install_module_step5_verify_rgb_result.SetLabelText("")
        self.label_install_module_step5_verify_rgbstatic_result.SetLabelText("")
        self.Layout()

