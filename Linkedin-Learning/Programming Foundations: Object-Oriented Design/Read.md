# ***Requirments***
mean what your application or product needs to do.  
  
### **functional requirements** 
* the system **must do**
* the application **must do**
___
## non-functional requirements
 that place constraints on how the application should function.  
 >### non--functional requirements  
* the system **should do**
* the application **should do**  

>###  **how should it to do it**
* legal
* performance
* Support
* Security   
 ### **On the first pass, only focus on capturing the absolute minimum set of requirements. Not the things are optional, or nice to have, or your dream features. Just the bare necessities, your minimum viable product.**

 ____
 ____
 ____
 # ***FURPS + requirement*** 
   FURPS serves as a checklist of several key qualities to consider when determining requirements.  
  ### **in short mean**  
    
 
  > **Functionality**  
   refers to the capabilities and Security and features of the app. 
   
  > **Usability**  
    affects the person who will be using the program. 

 
  > **reliability**   
 requirements, you'll need to know how much system downtime is acceptable. If the failures are predictable and how the system can be recovered.  

 > **Performance**  
  requirements dictate the application's response time through put. And they put limits on the system resources it can use.  

> **supportability**  
   application can be tested, extended, serviced and installed and configured.
___
## FURPS plus 
* **Design** addresses constraints on how the software must be built because the app requires certain things such as a relational database
* **Implemention** Does it have to be written in a certain language? Are there standards that need to be followed
* **Interface** refer an external system that needs to be interfaced with
* **Physical** constraints related to the hardware the application will be deployed on

 >**the purpose of FURPS plus**   
 is to prompt you to think about certain key requirement areas
 ___
 ___
 # ***Use Cases and User Stories***   
 ## Use cases
 * **Title:** what is the goal?
 * **primary actor:** who desiers it  
 * **Success Scenario:** How is it accomplished?  
 * **Extensions:** for th problem  

 
 >There isn't a single right way to write use cases 
 ---

## User stories
* As a(typeof user)
* I want (goal)
* So that (reason) **thise is optional**
___
___
# Domain Modeling
### Conceptual Model
Represents important objects and the relationships between them
___
## CRC cards
>stands for:
* Class
* Responsibility 
* Collaboration  

  **CRC cards contain the same information as the Conceptual Object Diagram, just in a different format.**

---
### **CRH cards**
>stands for:
* Component
* Responsibilities 
* Helper   

  **Those are effectively the same thing, just using different terms.**  
  ___
## constructor
 **It's a special method that gets called when the object is instantiated to help configure it.**

## multiple constructors  
 **have more than one method with the same name, but different sets of input parameters.**  

##  destructor 
**is a special method that gets called when an object is no longer needed and and is being disposed of.**  

## finalizer 
**rather than a destructor, but the concept is the same. It's a place to put some code that will automatically be called when the object is destroyed.**  
## instance variable
 **Variable for which  each instantiated object of Class has a separate copy**

## static variable
  * **which is a variable that's shared across all objects in the same class**   
  * **This is also referred to as a class level or shared variable.**  

     Python doesn't use the static keyword. 