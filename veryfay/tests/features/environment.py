import sys, os
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../../..')
sys.path.insert(0, my_path + '/steps')

from veryfay import *
from fixtures import *


def before_step(context, step):
    context.ae = \
    AuthorizationEngine() \
    .register(CRUDP()).allow(Admin).deny(Supervisor, Commiter).deny(Contributor).And \
    .register(CRUDP(SomeOtherClass)).allow(Admin).allow(Supervisor).allow(Reader).allow(Contributor).And \
    .register(Create()).allow(Commiter).deny(Contributor).And \
    .register(Read()).allow(Commiter).deny(Contributor).allow(Reviewer).And \
    .register(Read(SomeClass)).allow(Supervisor, Commiter).And \
    .register(Read(SomeClass), Read(SomeOtherClass)).allow(Supervisor).allow(Contributor).deny(Reader).And \
    .register(Read(SomeClass)).allow(Reader).And \
    .register(Read(OtherSomeOtherClass)).allow(Reader).deny(Commiter).allow(Reviewer).And \
    .register(Update(OtherSomeOtherClass)).deny(NoContainsRole).And \
    .register(Delete(OtherSomeOtherClass)).allow(NoContainsRole).And \
    .register(Update(SomeOtherClass)).deny(ContainsNoParamsRole).And \
    .register(Delete(SomeOtherClass)).allow(ContainsNoParamsRole).And \
    .register(Update(OtherClass)).deny(ContainsReturnNoBoolRole).And \
    .register(Delete(OtherClass)).allow(ContainsReturnNoBoolRole).And

