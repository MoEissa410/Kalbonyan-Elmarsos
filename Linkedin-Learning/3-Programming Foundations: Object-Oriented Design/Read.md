# Programming Foundations: Object-Oriented Design   
___

## Why do we use object orientation?   
___ 

* Programs used to be procedural (the program was written as a long procedure) 

* As programs became larger, this became difficult to manage. That's when object oriented programming was introduced (80s).  

* Large programs were split into objects. Each object represents a different part of the application and each object has its own data & logic, and they communicate with each other.  

### Other programming paradigms (mainly used in academics):

* logic programming language (Prolog)  

* functional programming language (Haskell)  

## What is an object?    
___
### **Objects have 3 things:**
* identity
* attributes
* behavior  

Objects in a computer are self contained. Identity -> They have an identity separate from other objects. Attributes -> information that describes their current state Behavior -> things they can do

## What is a class?
____
A class is a blueprint for an object. It describes attributes and behaviors.

## 4 Fundamental Ideas in Object-Oriented Programming:  
___
 * Abstraction
 * Polymorphism
 * Inheritance
 * Encapsulation  

in short mean APIE

### **What is abstraction?**
Abstraction means we focus on the essential qualities of something rather than one specific example. It also means we can have an idea or concept that is completely separate from any specific instance.

### **What is encapsulation?**  

It is restricting access to the inner workings of a class or objects based on that class. Also known as information hiding or data hiding.

Reason for encapsulation: to reduce dependencies between different parts of the application so that a change in one place won't cascade down and require multiple changes elsewhere.

### **What is inheritance?**  

When you create a class based on an existing class so that the child inherits attributes and behaviors from the parent.

### **What is polymorphism?**
Polymorphism means many forms. It lets us do the correct behavior even if what we're working with could take one of many different forms.

Example: + could add 2 integers. It can also concatenate 2 strings.

## Identifying classes in an application   
___
Typical approach:

* Gather requirements.
* Describe the app.
* Identify the main objects.
* Describe the interactions.
* Create a class diagram.
### **1. Gather requirements**
* What does the app need to do?
* What problem are you trying to solve?
* Write this down.
### **2. Describe the app**
* build a simple narrative of how people   
  * will use the app
  * use cases
  * user stories
* may or may not create a prototype
### **3. Identify the main objects**
use stories and descriptions from step 2 to identify the most important things/ideas of the app. Many of these things will become classes.
### **4. Describe the interactions**
formally describe the interactions between objects
Example: our customer needs to open a bank account.
This helps in identifying what methods will be needed
This could be done with a sequence diagram
### **5. Create a class diagram**
a visual representation of the classes you need
in interative approach, theses steps are revisited and refined throughout the development process

___
___

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

class Dog():  

      def __init__(self):  
    #instance variables
      self.breed=""
       self.weight=50
    #methods
---
