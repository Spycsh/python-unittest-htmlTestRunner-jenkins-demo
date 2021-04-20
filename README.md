# python-unittest-htmlTestRunner-jenkins-demo

* no CSS found in html report
It's because some in-line CSS is forbidden in Jenkins.  
Solution:
```
http://localhost:8080/script
```
In the text editor, add
```
System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
```
build again, report is integrated with CSS and elegantly shown.
