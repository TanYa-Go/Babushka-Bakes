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

# **Code Validation**

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
All the python files were validated with the [Pep8 Python validator](pep8)

Most common errors / warnings were:
* Blank line contains whitespace
* Trailing whitspace
* Line too long - some of which could not be corrected as it would break the code
* Missing docstring
* Unused imports
* No new line at the end of file
* Expected two blank lines, found one
* Too many blank lines

Majority of the errors and warnings was fixed, however some still remain, becasue breaking those lines would break the code:
* "Line too long" in migration files
* "Line too long" in settings file
* "Avoid using null=True on string-based fields such CharField" in some models

<br><br>

# **Responsiveness**


## **Test**
I was regularly checking responsiveness during development with Chrome developer inspector tools.\
I have tested the deployed site with help of the app called [Responsively](https://responsively.app/)
Test was also done on the actual devices: Lenovo Laptop 17.3" / Alpha a1 20+ / Xiaomi Redmi 9t /  iPhone 7 / iPhone 8 / iPhone 10 / iPad 

## **Result**
The page looks satisfactory on all tested devices and is fully responsive. The Navigation menu collapses on tablet and mobile sizes and expands on desktop size. Hero image is not destorted and displays nicely on all screen sizes tested. 

Images on all other pages are responsive, they are rendering well on all screen sizes tested without overflowing or distorsion.
Text responsiveness is satisfactory.

## **Conclusion**
Test result is satisfactory, everything is functioning as intended.

<br>
<br>

# **User Stories**

## **Navigation and rensponsiveness**
### **All users** 

User Story:
* *To have a website that is clean and easy to navigate and displays well on all devices*


Responsiveness was covered in the separate section above, and the results are satisfactory.

Navigation bar is visible on all pages of the website  which makes it easy for user to browse around and contributs to a smoother user experience.

On smaller sizes, the navigation menu collapses to a hamburger button which expands on click. 

To test navigation, I have tested the following:

**Navigation menu items**

* Clicked on each navigation menu item to make sure that they each lead to their respective pages. 

* Clicked on the **View Shop** and **Contact Me** buttons to make sure that they leed to their respective pages. 

**Footer menu items**

* Clicked on each navigation menu item in the footer to make sure that they lead to their respective pages. 

**Social Media Icons**

* Clicked on each social media icon in the footer to make sure that they lead to their respective pages. 

**Buttons**

* Clicked on each button on all pages of the website to make sure they will lead to the relevant page. 

**Brand Name**

* To return to the **Home** Page, the user can click on the brand name in the top left corner and will be redirected to the home page. 


## **Result** : 

No broken links in navbar, all pages open as expected.\
**Shop** link opens a dropdown menu on hover, as expected.\
Social media icons lead to their respective generic page and open in a separate tab.\
All buttons work as expected and lead to their respective pages.

Test passed, all functions work as expected.

<br><br>

## **Account Creation and Profile Management**
### **Site Visitor**

This is first time visitor as well as a returning visitor who hasn't created an account previously.

* User Story:
    * *As a	site visitor I want to be able to:*
         * *Easily register for an account so that I can have my account and view my profile.*
        * *Easily login and logut* 
        * *Easily recover my password if neccesary*



The **My Account** icon is placed in the website header and it is clearly visible and accessible from any page of the website.

Visitor can click on the **My Account** icon and will see the options to **Login** or **Register**

When the visitor clicks on **Register** they will be presented with a  form asking for their details. After submitting the form, an email confirmation will be required. When the visitor confrims their email, they will be able to log in with their new credentials.

As a **logged-in** user, the user can now see additional option in the **My Account** dropdown menu - **Profile Management**. From here the user can update their profile information that are saved for future purchases.

In case the user forgets their password, they can click on the **Forgot Password?** link and follow the instructions to change the password.

When finished, the user can easily log out by clicking the **Logout** link in the **My Account** menu. They will be asked to confrim if they really want to logout in case they have clicked this link by accident.  

### **Result** : 
I have followed the proces several times and creates several users. The process is simple and intuitive and the visitor can create their account with a few clicks, easily manage their profile and logout.

Test passed, the function works as expected. 


<br>

## **Contact**

* User Story:
    * *As a user I want to contact the store owner to ask a question regarding products or place a custom order*

The user can contact the site owner easily with a few options. There is a **Contact** menu item in the navabr that will lead to the **Contact Page**. There is also a menu link in the footer, available on each page, apart from home page, that also leads to the Contact Page. On the home page, the user has the **Contact Me** button, as well as the navbar menu link to Contact Page.

When on the contact page, the user has a few options for contact. They can fill out the contact form and their message will land directly in the site owners email.\
There is a contact number, an email address as well as the postal address, should that be their preffered way of contacting. 

The user also has the **Social Media** option to contact the site owner. Currently the links lead to generic pages but in the future, the actual Petra's social media handles are to be added. 

### **Result** : 
I have tested all the links and they all correctly lead to the Contact Page. I have also sent several emails from the contact form and confirmed that the email is indeed sent, and recieved by the site owner (my own email in this case).

Test passed, the function works as expected. 

## **The Blog**

* User Story:
    * I want to be able to read the latest blog posts, so I can find some reciepts that I can try to bake myself   

The blog is accesible by the Navbar menu link. /The link leads to the **Blog Page** that has all the blog posts listed. 

**Logged in user**  can see the options to create a new blog post, edit and/or delete an existing blog post.

All buttons were tested and they lead to relevant pages.

**User that is not logged in** will not see those options and will only be able to read the blog. 




<br><br>

# **Functionality**



# **Bugs**