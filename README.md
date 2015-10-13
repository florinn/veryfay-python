Veryfay (Python) [![build badge](https://travis-ci.org/florinn/veryfay-python.svg?branch=master)](https://travis-ci.org/florinn/veryfay-python)
===================

**Veryfay (Python)** is a port to Python of the [**Veryfay**](https://github.com/florinn/veryfay-scala) library in Scala.

----------


Features
-------------
* Define multiple authorization engines in the same application
* Define activities with or without a target class
* Specify allow or deny sets
* Associate roles to multiple activities through hierarchical activity containers
* Check authorization either by returning boolean or exception throwing


Installing
-------------
**Veryfay requires Python >= 3.3 **

A universal installation method (that works on Windows, Mac OS X, Linux) is to use [pip](https://pip.pypa.io/en/latest/): 

```
$ pip install --upgrade veryfay 
```

Or download the source files to a local dir, cd to that dir and run:
```
$ python setup.py install
```

Usage
-------------

### Define authorization rules

This part consists of a few straightforward preparatory operations that culminate with the creation of an "authorization engine" to be used later to perform authorization verification.

##### Define any custom activities

An activity takes a class parameter as the target for the activity, which may be any class defined in your application.

For activities with no target, you should omit the argument of the activity.

There are a few predefined activities: 
- *Create*
- *Read*
- *Update*
- *Patch*
- *Delete*

You may define your own activities by inheriting from `Activity`:

```python
class SomeActivity(Activity):
    pass
```

##### Define any container activities

Container activities help with associating multiple actions to the same role(s).  
Instead of repeating the same activities over and over again, a container activity may be defined holding a list of activities (including container activities).

There a couple predefined container activities:
- *CRUD* containing activities: *Create*, *Read*, *Update*, *Delete*
- *CRUDP* containing activities: *CRUD*, *Patch*

Define your own container activities like so:

```python
class CRUD(Container):

    def __init__(self, target=None):
        activities = [SomeActivity(target), OtherActivity(target), SomeOtherActivity(target)]
        return super().__init__(activities)
```

>**Note:** Container activities are used only for defining authorization rules, they are not used when verifying authorization rules

##### Define roles

You can define a role by defining a class with a 'contains' method that:
- takes as parameters a 'principal' object and any extra info using the extended formal argument syntax
- returns a boolean value 

In the `contains` method you can place any logic to determine if the input data belongs to that role.

```python
class SomeRole(object):
    
    def contains(self, principal, *extra_info):

        # Some logic to determine if input belongs to the role
        # return boolean
```

##### Configure authorization rules 

You may use `register`, `allow`, `deny` and `And` to associate any allow and deny roles with one or more activities in the context of an authorization engine:

```python
ae = \
    AuthorizationEngine() \
    .register(CRUDP()).allow(Admin).deny(Supervisor, Commiter).deny(Contributor).And \
    .register(CRUDP(SomeOtherClass)).allow(Admin).allow(Supervisor).allow(Reader).allow(Contributor).And \
    .register(Create()).allow(Commiter).deny(Contributor).And \
    .register(Read()).allow(Commiter).deny(Contributor).allow(Reviewer).And \
    .register(Read(SomeClass)).allow(Supervisor, Commiter).And \
    .register(Read(SomeClass), Read(SomeOtherClass)).allow(Supervisor).allow(Contributor).deny(Reader).And \
    .register(Read(SomeClass)).allow(Reader).And \
    .register(Read(OtherSomeOtherClass)).allow(Reader).deny(Commiter).allow(Reviewer).And
```

>**Notes:** 
- `allow` and `deny` can take as parameters either class instances or class objects with a no param constructor.
- Roles specified in the same argument list of `allow` or `deny` are bound together by logical *AND*
- Roles specified in separate argument lists of `allow` or `deny` are bound together by logical *OR*


### Verify authorization rules

To verify the authorization rules you may call either: 

- `is_allowing` returns **IsAllowingResult** containing the result of the verification as a bool value and a string with information about the execution of the authorization rules

```python
result = ae(Read(SomeClass)).is_allowing(PrincipalClass('reader'), 1234)
```
 
- `verify` returns a **string** in case of success, otherwise throws **AuthorizationException** containing a string with information about the execution of the authorization rules

```python
ae(Read(OtherSomeOtherClass)).verify(OtherPrincipalClass('reader'), 1234, "1234")
```

>**Note:** During rules verification, if a role definition lacks a `contains(self, principal, *extra_info)` method that returns a boolean value, a **NotImplementedError** exception is thrown