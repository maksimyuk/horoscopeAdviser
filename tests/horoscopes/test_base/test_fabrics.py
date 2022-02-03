from server.horoscopes.base.fabrics import (
    BaseRequestFabric,
    SignDrivenRequestFabric,
)
from server.horoscopes.enums import HoroscopeSigns


class TestRequestFabric(BaseRequestFabric):
    """Fabric for test purposes."""

    base_url = "http://test.com"


class TestSignDrivenRequestFabric(SignDrivenRequestFabric):
    """Fabric for test purposes with sign param."""

    base_url = "http://testsign..com"


class TestBaseRequestFabric:
    """Tests for base fabric class."""

    def test_init_by_empty_params(self):
        """Check default init params for empty params and data."""
        fabric = TestRequestFabric()

        assert fabric.params == {}
        assert fabric.data == {}

    def test_base_prepare_request(self):
        """Check base prepare_request_url returns base_url."""
        fabric = TestRequestFabric()

        assert fabric.prepare_request_url() == TestRequestFabric.base_url

    def test_create_empty_request(self):
        """Check created request has no params, no data."""
        fabric = TestRequestFabric()

        request = fabric.create()

        assert not request.data
        assert not request.params

    def test_create_request_with_params(self):
        """Check created request has params, no data."""
        fabric = TestRequestFabric(params={"param1": "test"})

        request = fabric.create()

        assert request.params
        assert not request.data

    def test_create_request_with_data(self):
        """Check created request has data, no params."""
        fabric = TestRequestFabric(data={"data": "test"})

        request = fabric.create()

        assert request.data
        assert not request.params

    def test_create_request(self):
        """Check created request has data and params."""
        fabric = TestRequestFabric(data={"data": "test"}, params={"param1": "test"})

        request = fabric.create()

        assert request.data
        assert request.params


class TestBaseSignDrivenRequestFabric:
    """Tests for base fabric class with sign parameter."""

    def test_init(self):
        """Check request fabric is initiated with given sign enum."""
        fabric = TestSignDrivenRequestFabric(sign=HoroscopeSigns.CANCER)

        assert fabric.sign == HoroscopeSigns.CANCER
