import pytest

@pytest.mark.skip(reason="reason for skipping the test case")
def test_with_introspection(introspective_fixture):
    print("\nRunning test_with_introspection...")
    pytest.fail("Wrong data type passed")
    assert True


@pytest.fixture
def introspective_fixture(request):
    """
    The request fixture allows introspection into the
    "requesting" test case
    """
    print("\n\nintrospective_fixture:")
    print("...Called at {}-level scope".format(request.scope))
    print("   ...In the {} module".format(request.module))
    print("      ...On the {} node".format(request.node))
