# certutil

#### open cert manager for the local machine
```c
certlm
```
#### Request, convert certificate & extract keys
```powershell
#list template from CA
certutil -dump | sls 'config:' # dump CA config
certutil -CATemplates -config <CA Enterprise machine>

```


```shell
certutil -addstore -f "ROOT" new-root-certificate.crt
certutil -delstore "ROOT" serial-number-hex
```

In some remote access scenarios it is not possible to copy binary data (such as files) but you can copy\transfer plain text, Base64 is a better choice.

#### convert binary (pfx) file to Base64 (.cer) with powershell

```powershell
Get-PfxCertificate -FilePath F:\Certs\ServerCerts\demosite.org.pfx | Export-Certificate -FilePath F:\Certs\ServerCerts\demosite.cer -Type CERT
```

#### convert Binary CER file to  *.PEM file which is ASCII file
```c
certutil.exe -encode .\demosite.cer demosite1.cer
certutil -encode filename.cer newfilename.cer
```

#### Convert from Base64 to Binary
```c
certutil -decode filename.cer newfilename.cer
```




