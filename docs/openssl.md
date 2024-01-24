# openssl
openssl command makes is easier to manipulate certificates.

[OpenSSL site](https://openssl.org)

***DER*** encoded binary X.509(.CER) is called ***D***istinguished ***E***ncoding ***R***ules which is a binary format.
***Base64*** which is an encoding method that converts binary data to plain ASCII text.

The *.CER extension is interchangeable with *.CRT

Sometimes,

* DER certificate have *.der extension
* Base64 have *.pem extension

Open in text editor

* DER gibberish
* Base64 ASCII code

#### openssl to extraxt certificate file & private key from PFX file
- Make PFX file from install certificate on Windows system
- copy it to Linux machine
- Create the cert file 

```bash
sudo openssl pkcs12 -in <pfx_filename.pfx> -out certificate.crt -nokeys 
```
- creates private key
```bash
sudo openssl pkcs12 -in certificate.p12 -out privateKey.key -nodes -nocertsopenssl pkcs12 -in certificate.p12 -out privateKey.key -nodes -nocerts
```

[https://sslhow.com/openssl-pkcs12](https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsslhow.com%2Fopenssl-pkcs12&data=05%7C01%7CE.Aziz%40soton.ac.uk%7C4062f2e9744b4ddcc7db08dab381c414%7C4a5378f929f44d3ebe89669d03ada9d8%7C0%7C0%7C638019667157725226%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=g6BQimcmJYlNbEQTk5cyXuMIg211xkNyhO%2F1TOBPv0Q%3D&reserved=0 "Original URL: https://sslhow.com/openssl-pkcs12. Click or tap if you trust this link.")

#### Another method, extracting Certificate & keys

- extract private key (Encrypted)
```bash
sudo openssl pkcs12 -in <pfx_filename.pfx> -nocerts -out <keyfilename-encrypted.key>
```
            
- Extract certificate from pfx file
```bash
sudo openssl pkcs12 -in pfx_filename.pfx -clcerts -nokeys -out <certifcate_file_name>.crt
```

- Extract private Unencrypted format from Encrypted private key file
```bash
sudo openssl rsa -in keyfilename-encrypted.key -out keyfilename-decrypted.key
```

[https://bobcares.com/blog/convert-pfx-to-crt-key-files/](https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fbobcares.com%2Fblog%2Fconvert-pfx-to-crt-key-files%2F&data=05%7C01%7CE.Aziz%40soton.ac.uk%7C4062f2e9744b4ddcc7db08dab381c414%7C4a5378f929f44d3ebe89669d03ada9d8%7C0%7C0%7C638019667157725226%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=04ReTHk1rwYRBG6e%2B7fYiGnFHRr81YNDVFjheB%2FZXrY%3D&reserved=0 "Original URL: https://bobcares.com/blog/convert-pfx-to-crt-key-files/. Click or tap if you trust this link.")

### Convert using openssl command

#### If the certificate file Base64 (.cer extension) which is PEM format
```bash
sudo openssl x509 -inform PEM -in BASE64_cert.cer -out NEW_Cert_File_Name.crt
```

#### If the certificate file in DER format (.cer extension)
```bash
sudo openssl x509 -inform DER -in DER_cert.cer -out NEW_Cert_File_Name.crt
```
**********************

### Check client TLS version and certificate with openssl

```bash
openssl s_client -connect bbc.co.uk:443
echo | openssl s_client -connect bbc.co.uk:443 2>/dev/null | openssl x509 -noout -dates #listing dates
echo | openssl s_client -connect bbc.co.uk:443 2>/dev/null | openssl x509 -text -noout | grep "Public-Key" #extract public key size
```
