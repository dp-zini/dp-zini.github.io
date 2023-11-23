def create_ahk_script(filename, script_content):
    with open(f"{filename}.ahk", "w") as file:
        file.write(script_content)
def create_bat_file(filename, content):
    with open(f"{filename}.bat", "w") as file:
        file.write(content)
block_script = "!f2::\nRun, blockhitman.bat\nreturn\n"
unblock_script = "!f1::\nRun, unblockhitman.bat\nreturn\n"
block_bat_content = "netsh advfirewall firewall set rule name=\"hitman\" new enable=yes\n"
unblock_bat_content = "netsh advfirewall firewall set rule name=\"hitman\" new enable=no\n"
create_ahk_script("blockhitman", block_script)
create_ahk_script("unblockhitman", unblock_script)
create_bat_file("blockhitman", block_bat_content)
create_bat_file("unblockhitman", unblock_bat_content)