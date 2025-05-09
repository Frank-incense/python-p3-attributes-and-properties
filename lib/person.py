#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Frank", job="ITC"):
        self.name = name
        self.job = job

    def getname(self):
        print("Retrieving name")
        return self._name
    
    def setname(self, name):
        if type(name) is str and name and 0 < len(name) < 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    
    def getjob(self):
        print("Retrieving job")
        return self._job
    
    def setjob(self, job):
        if job in APPROVED_JOBS and job:
            self._job = job
        else: 
            print("Job must be in list of approved jobs.")

    name = property(getname, setname)
    job = property(getjob, setjob)
