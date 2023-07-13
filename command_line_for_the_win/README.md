Secure File Transfer Protocol (SFTP)
Secure File Transfer Protocol (SFTP) is a network protocol for securely accessing, transferring and managing large files and sensitive data.
How to use SFTP
open a command line terminal
type sftp "username@hostname"
Example:
sftp 407939ef5a69@407939ef5a.09417.alxcode

sftp commands
ls - lists the files in remote directory
lls - lists the files in your local machine
pwd - prints the remote server working directory
lpwd - prints the local working directory
cd - changes the remote working directory
lcd - changes directory in your local mechine
put - put is used to upload files from local mechine to remote server
put filename

mput - mput is used to upload multiple files from local mechine to remote server
Example upload all files that ends with .txt from local mechine to remote server
mput *.txt

get - get is used to download files from remote server to local mechine get filename

mget - mget is used to download multiple files from remote server to local mechine

Example download all files that ends with .txt from remote server to local mechine
mget *.txt
