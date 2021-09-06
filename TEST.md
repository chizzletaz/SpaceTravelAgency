Go to the [README file](https://github.com/chizzletaz/BakeAndBinge/blob/master/README.md)

# **Testing**
## Table of Contents
- [Testing User stories](#testing-user-stories)  
    * [First time users](#first-time-users)
    * [General users](#general-users)
    * [Regular users](#regular-users)
- [Testing Developer stories](#developer-stories)
    * [Admin/site owner](#adminsite-owner)
- [Manual testing features](#manual-testing-features)
- [Code Validation](#code-validation)  
    * [HTML](#html)
    * [CSS](#css)
    * [Javascript](#javascript)
    * [Python](#python)
- [Testing browser compatibility](#testing-browser-compatibility)  
- [Testing Responsiveness](#testing-responsiveness)  
- [Bugs and Problems](#bugs-and-problems)  
***

## Testing user stories
### First time users:
**1. As a first time user, I want to navigate easily across the website.**
- The user can navigate the website by using the links in the navbar.  
![navbar image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/navbar.png) 

## Manual testing features

**Subscription option**  
Expected:   
The user is subscribed to the newsletter when the user fills in the subscription form correctly.

Testing:
1. Go to the footer of any page (except register or login).
2. Don't fill in an email address and click 'Subscribe'.
3. Confirm that a warning message appears.  
   Result:  
        A 'Subcription successfull' message appears.  
   Fix:   
        Add 'required' to the input field.  
   Result:  
        A warning message appears.
4. Fill in an invalid email address.
5. Confirm that a warning message appears.
6. Fill in a valid email address.
7. Confirm that the message 'Subscription successful!' appears.
8. Fill in the same email address.
9. Confirm that the message 'Apparently you've subscribe already. This email already exists.' appears.

Result:  
The user is subscribed to the newsletter when the user fills in the subscription form correctly.

---
## Code validation
### HTML
[W3C Markup Validation Service](https://validator.w3.org/) is used to check for markup validity of the web document.  
Because Flask Jinja template is used on all HTML pages, the source code is taken from the rendered pages to be tested.  
You can validate the rendered page by:  
- Use the source code of the rendered page
    - Right click on the page
    - Click 'show source code'
    - Copy all HTML
    - Paste it into the validator. 

Or  
- Enter the url of the Heroku live link.

However, when authentication is used, the live link can't be used to validate the page.
Furthermore, the live site of Heroku takes a while to update.   
Therefore I've opted to use the source code to render the pages.

Running the code through the validator gives:  
#### For index.html:
- 4 errors and 1 warning shown  
![html index error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-index.png)
1. *Element `<h4>` not allowed as child of element `<ul>` in this context.*  
Fix:  
According to HTML5 spec, you can't have header tags as children within a `<ul></ul>`, you can only have `<li>` elements as children. So you should populate it with `<li></li>`, then insert your content within each list, so wrap the h4 in `<li></li>`  
Credit: [Mike Hanslo](https://stackoverflow.com/questions/29079953/element-h4-not-allowed-as-child-of-element-ul-in-this-context)
2. *Section lacks heading.*   
Fix:  
Change section into div.
3. *Start tag `<a>` seen but an element of the same type was already open.*  
I originally only had the 'go to recipe'-button acting as an anchor tag. Later I added an anchor tag to the whole card, but forgot to remove the anchor tag of the button. This resulted in an anchor tag inside another anchor tag.   
Fix:  
Change the the anchor tag of the button to a button tag and remove the href.  
This gives another error:  
4. *The element button must not appear as a descendant of the a element.*    
Fix:  
Change button tag to `<p>` tag with button class.
> Note: Since similar cards are used on the recipes and profile pages pages, these errors will be fixed there as well.

---
### CSS  
[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) is used to check the CSS of the web document.
Running the code through the validator gives:
#### For style.css:
- No errors are found.  
![style.css validation](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/css-style.png)

---
### Javascript  
[JSHint](https://jshint.com/) is used to check the validity of the Javascript of the web document.  
It is recommended to add **```/* jshint esversion: 6 */```** at the top of the .js file to tell JSHint that your code uses ECMAScript 6 specific syntax.  

Running the code through the validator gives:
#### For style.js:
- No errors or warnings are shown. 
---
### Python  
[PEP8 online](http://pep8online.com/) is used to check the python code for PEP8 requirements.
#### For app.py:
Before checking the app.py file, I tried to remove as many mistakes beforehand, such as extra whitespaces, maximum
code line length of 72, correct line breaks, etc. Nevertheless, there were a lot of issues that I missed.  
- Several notifications  
![pep8 python notifications](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/python-pep8.png)  
After fixing the notifications, I get an All right message.
![All right message pep8](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/python-pep8-after.png)

---
## Testing browser compatibility
I've tested the website on Safari, Chrome and Mozilla Firefox.  
The testing was done by:

- Visually checking the pages.
- Checking all links.
- Checking CRUD functionality.

No issues arose during testing.  

---
## Testing responsiveness
To test the responsiveness of the  website, I've used Chrome Dev Tools by:
- right clicking on the page
- click inspect 
- click toggle device toolbar  
![toggle device toolbar button](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/toggle-device-toolbar.png)  
- select the different devices.  
![responsive choices](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/responsive.png)

and [Responsinator](https://www.responsinator.com/) to test the site at different screen resolutions.   

The testing was done on widths down to a screen resolution of 280px.  
All the elements on each page were checked.  

No issues arrose.

## Bugs and problems

Issue: SOLVED  
The 'Recipes' dropdown menu in the navbar doesn't adapt to the width of the text inside and a vertical scroll bar is displayed.  
Furthermore, when clicking on the 'Recipes', the name disappears.  

Fix:  
According to the documentation of Materialize, you can change the ![constrainWidth](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/README/images/contrainwidth.png).  
add: { constrainWidth: false } as an option to $(".dropdown-trigger").dropdown() (the dropdown trigger in the javascript file).  

Extra: looking at the other options, I added ![coverTrigger](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/README/images/covertrigger.png), so the dropdown menu will display below the trigger.   
And ![hover](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/README/images/hover.png), so the dropdown menu will open on hover.  

> UPDATE: I removed hover from the dropdown menu, cause on mobile devices the dropdown didn't work.
  