# code 

## for exception

in window you need to dowload java and config like 

Go to Start → Control Panel → System → Advanced system settings → advanced(tab) → Environment Variables → System Variables → New:
```
Variable name: _JAVA_OPTIONS
Variable value: -Xmx512M 
```
and in System Variables choose Path add `C:\Program Files (x86)\Java\jre1.8.0_231\bin` then ok -> ok,  Done 

to run check you should restart cmd and run `java -version` if success if will out your java 