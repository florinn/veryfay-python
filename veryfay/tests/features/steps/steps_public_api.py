from behave import when, then
from hamcrest import assert_that, calling, raises

from veryfay import *
from fixtures import *


@when('action target not found')
def step_impl(context):
    pass


@then('it should fail when action target not found')
def step_impl(context):
    result = context.ae(Create(SomeClass)).is_allowing(PrincipalClass('commiter'))
    assert_that(calling(context.ae(Create(SomeClass)).verify).with_args(PrincipalClass('commiter')), raises(AuthorizationException))
    assert_that(result.is_failure)


@when('action target found')
def step_impl(context):
    pass


@then('it should fail when target type not matching')
def step_impl(context):
    result = context.ae(Read(OtherSomeOtherClass)).is_allowing(PrincipalClass('supervisor'))
    assert_that(calling(context.ae(Read(OtherSomeOtherClass)).verify).with_args(PrincipalClass('supervisor')), raises(AuthorizationException))
    assert_that(result.is_failure)


@when('deny role found')
def step_impl(context):
    pass


@when('deny role found once')
def step_impl(context):
    pass


@then('it should fail when principal match the deny role definition')
def step_impl(context):
    result = context.ae(Read()).is_allowing(OtherPrincipalClass('contributor'))
    assert_that(calling(context.ae(Read()).verify).with_args(OtherPrincipalClass('contributor')), raises(AuthorizationException))
    assert_that(result.is_failure)


@then('it should fail when principal and extra info match the deny role definition')
def step_impl(context):
    result = context.ae(Read(SomeClass)).is_allowing(PrincipalClass('reader'), 1234)
    assert_that(calling(context.ae(Read(SomeClass)).verify).with_args(PrincipalClass('reader'), 1234), raises(AuthorizationException))
    assert_that(result.is_failure)


@then('it should succeed when principal does not match every deny role definition in a set')
def step_impl(context):
    result = context.ae(Create()).is_allowing(PrincipalClass('commiter'))
    context.ae(Create()).verify(PrincipalClass('commiter'))
    assert_that(result.is_success)


@then('it should fail when principal match every deny role definition in a set')
def step_impl(context):
    result = context.ae(Create()).is_allowing(PrincipalClass('supervisor-commiter'))
    assert_that(calling(context.ae(Create()).verify).with_args(PrincipalClass('supervisor-commiter')), raises(AuthorizationException))
    assert_that(result.is_failure)


@then('it should fail when a matching deny role definition does not define a "contains" method')
def step_impl(context):
    assert_that(calling(context.ae(Update(OtherSomeOtherClass)).is_allowing).with_args(PrincipalClass('supervisor')), raises(NotImplementedError))
    assert_that(calling(context.ae(Update(OtherSomeOtherClass)).verify).with_args(PrincipalClass('supervisor')), raises(NotImplementedError))


@then('it should fail when a matching deny role definition has a "contains" method that does not take at least one parameter')
def step_impl(context):
    assert_that(calling(context.ae(Update(SomeOtherClass)).is_allowing).with_args(PrincipalClass('commiter')), raises(NotImplementedError))
    assert_that(calling(context.ae(Update(SomeOtherClass)).verify).with_args(PrincipalClass('commiter')), raises(NotImplementedError))


@then('it should fail when a matching deny role definition has a "contains" method that does not return a boolean value')
def step_impl(context):
    assert_that(calling(context.ae(Update(OtherClass)).is_allowing).with_args(PrincipalClass('commiter')), raises(NotImplementedError))
    assert_that(calling(context.ae(Update(OtherClass)).verify).with_args(PrincipalClass('commiter')), raises(NotImplementedError))


@when('deny role found more than once')
def step_impl(context):
    pass


@then('it should fail when principal and any extra info match any deny role definition')
def step_impl(context):
    result = context.ae(Read()).is_allowing(OtherPrincipalClass('contributor'))
    assert_that(calling(context.ae(Read()).verify).with_args(OtherPrincipalClass('contributor')), raises(AuthorizationException))
    assert_that(result.is_failure)


@then('it should fail when principal and any extra info match any contained deny role definition')
def step_impl(context):
    result = context.ae(Patch()).is_allowing(OtherPrincipalClass('contributor'))
    assert_that(calling(context.ae(Patch()).verify).with_args(OtherPrincipalClass('contributor')), raises(AuthorizationException))
    assert_that(result.is_failure)


@then('it should fail when principal and any extra info match any deny role definition in an embedded container action')
def step_impl(context):
    result = context.ae(Delete()).is_allowing(OtherPrincipalClass('contributor'))
    assert_that(calling(context.ae(Delete()).verify).with_args(OtherPrincipalClass('contributor')), raises(AuthorizationException))
    assert_that(result.is_failure)


@when('deny role not found')
def step_impl(context):
    pass


@when('allow role not found')
def step_impl(context):
    pass


@then('it should fail when allow role not found')
def step_impl(context):
    result = context.ae(Read(SomeClass)).is_allowing(PrincipalClass('laura'))
    assert_that(calling(context.ae(Read(SomeClass)).verify).with_args(PrincipalClass('laura')), raises(AuthorizationException))
    assert_that(result.is_failure)


@when('allow role found')
def step_impl(context):
    pass


@when('allow role found once')
def step_impl(context):
    pass


@then('it should succeed when principal match an allow role definition')
def step_impl(context):
    result = context.ae(Read(SomeOtherClass)).is_allowing(OtherPrincipalClass('contributor'))
    context.ae(Read(SomeOtherClass)).verify(OtherPrincipalClass('contributor'))
    assert_that(result.is_success)


@then('it should succeed when principal and extra info match an allow role definition')
def step_impl(context):
    result = context.ae(Read(OtherSomeOtherClass)).is_allowing(OtherPrincipalClass('reader'), 1234, "1234")
    context.ae(Read(OtherSomeOtherClass)).verify(OtherPrincipalClass('reader'), 1234, "1234")
    assert_that(result.is_success)


@then('it should fail when principal does not match every allow role definition in a set')
def step_impl(context):
    result = context.ae(Read(SomeClass)).is_allowing(PrincipalClass('commiter'))
    assert_that(calling(context.ae(Read(SomeClass)).verify).with_args(PrincipalClass('commiter')), raises(AuthorizationException))
    assert_that(result.is_failure)


@then('it should succeed when principal does match every allow role definition in a set')
def step_impl(context):
    result = context.ae(Read(SomeClass)).is_allowing(PrincipalClass('supervisor-commiter'))
    context.ae(Read(SomeClass)).verify(PrincipalClass('supervisor-commiter'))
    assert_that(result.is_success)


@then('it should fail when a matching allow role definition does not define a "contains" method')
def step_impl(context):
    assert_that(calling(context.ae(Delete(OtherSomeOtherClass)).is_allowing).with_args(PrincipalClass('supervisor')), raises(NotImplementedError))
    assert_that(calling(context.ae(Delete(OtherSomeOtherClass)).verify).with_args(PrincipalClass('supervisor')), raises(NotImplementedError))


@then('it should fail when a matching allow role definition has a "contains" method that does not take at least one parameter')
def step_impl(context):
    assert_that(calling(context.ae(Delete(SomeOtherClass)).is_allowing).with_args(PrincipalClass('commiter')), raises(NotImplementedError))
    assert_that(calling(context.ae(Delete(SomeOtherClass)).verify).with_args(PrincipalClass('commiter')), raises(NotImplementedError))


@then('it should fail when a matching allow role definition has a "contains" method that does not return a boolean value')
def step_impl(context):
    assert_that(calling(context.ae(Delete(OtherClass)).is_allowing).with_args(PrincipalClass('commiter')), raises(NotImplementedError))
    assert_that(calling(context.ae(Delete(OtherClass)).verify).with_args(PrincipalClass('commiter')), raises(NotImplementedError))


@when('allow role found more than once')
def step_impl(context):
    pass


@then('it should succeed when principal and any extra info match any allow role definition')
def step_impl(context):
    result = context.ae(Read(SomeClass)).is_allowing(PrincipalClass('supervisor'))
    context.ae(Read(SomeClass)).verify(PrincipalClass('supervisor'))
    assert_that(result.is_success)


@then('it should fail when principal and any extra info do not match any allow role definition')
def step_impl(context):
    result = context.ae(Create(OtherSomeOtherClass)).is_allowing(PrincipalClass('commiter'))
    assert_that(calling(context.ae(Create(OtherSomeOtherClass)).verify).with_args(PrincipalClass('commiter')), raises(AuthorizationException))
    assert_that(result.is_failure)


@then('it should succeed when principal and any extra info match any contained allow role definition')
def step_impl(context):
    result = context.ae(Patch(SomeOtherClass)).is_allowing(PrincipalClass('admin'))
    context.ae(Patch(SomeOtherClass)).verify(PrincipalClass('admin'))
    assert_that(result.is_success)


@then('it should succeed when principal and any extra info match any allow role definition in an embedded container action')
def step_impl(context):
    result = context.ae(Delete(SomeOtherClass)).is_allowing(PrincipalClass('admin'))
    context.ae(Delete(SomeOtherClass)).verify(PrincipalClass('admin'))
    assert_that(result.is_success)
