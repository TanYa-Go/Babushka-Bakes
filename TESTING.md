# **Testing**

## Table of contents 
* [Code Validation](#code-validation)
* [Responsiveness](#responsiveness)
* [User Stories](#user-stories)
* [Functionality](#functionality)
    * [My Profile](#my-profile)
    * [Shop](#shop)
    * [Navigation](#navigation)
    * [Footer](#footer)
    * [Search](#search)
    * [Blog](#blog)


<br/>

## **Code Validation**

### **HTML**
All the HTML files were validated with [HTML Validator](https://validator.w3.org/). There was only a few minor errors such as double closing tags or missing tags. These errors were fixed and there are no errors or warnings left. 

### **CSS**
All the CSS files have passed the [CSS Validator](https://jigsaw.w3.org/css-validator/) without issues.

### **JavaScript**
All the javascript were validated with the [Javascript Validator](https://jshint.com/) 

* Missing semicolon was added
* Undefined variable ($) warning was not changed or fixed as it would lead to code not working  
* The warning 'template literal syntax' is only available in ES6 (use 'esversion: 6'), was fixed by changing jshint configuration to ES6


### **Python**
All the python files were validated with the [Python validator](pep8)

Most common errors / warnings were:
* Blank line contains whitespace
* Trailing whitspace
* Line too long - some of which could not be corrected as it would break the code
* Missing docstring
* Unused imports
* No new line at the end of file
* Expected two blank lines, found one
* Too many blank lines

Majority of the errors and warnings was fixed, however some still remain:
* "Line too long" in migration files
* "Line too long" in settings file
* "Avoid using null=True on string-based fields such CharField" in some models




## **Responsiveness**


#### Test 
I was regularly checking responsiveness during development with Chrome developer inspector tools.\
I have tested the deployed site with help of the app called [Responsively](https://responsively.app/)
Test was also done on the actual devices: Lenovo Laptop 17.3" / Alpha a1 20+ / Xiaomi Redmi 9t /  iPhone 7 / iPhone 8 / iPhone 10 / iPad 

#### Result 
The page looks satisfactory on all tested devices and is fully responsive. The Navigation menu collapses on tablet and mobile sizes and expands on desktop size. Hero image is not destorted and displays nicely on all screen sizes tested. 

Images on all other pages are responsive, they are rendering well on all screen sizes tested without overflowing or distorsion.
Text responsiveness is satisfactory.



#### Conclusion
Test result is satisfactory, everything is functioning as intended.


## **User Stories**


* *Site visior/shopper's goal is to be able to easily browse the website on any device so that they can quickly find what they are looking for*

### **Test needed for: Navigation and rensponsiveness**

Responsiveness was covered in the above section and the results are satisfactory.

To test navigation, I have tested the following:

Navigation menu items 

* Clicked on each navigation menu item to make sure that they each lead to their respecive pages. 

* Clicked on the "View Shop" and "Contact me" button to make sure that they leed to their respective pages. 

Footer menu items 

* Clicked on each navigation menu item to make sure that they lead to their respecive pages. 

Social Media Icons

* Clicked on each icon in the footer to make sure that they lead to their respecive pages. 

Buttons

* Clicked on each button to make sure they will lead to the said page. 

Brand Name 

* When user is on any page except home page they can click on the Brand Name Logo and be redirected back to the home page. 


### Result : 

No links broken, all pages open as expected.\
**Shop** link opens a dropdown menu on hover, as expected.\
Social media icons lead to their respective generic page and open in a separate tab.\
All buttons work as expected and lead to their respective links.


## **Functionality**








## **Bugs**