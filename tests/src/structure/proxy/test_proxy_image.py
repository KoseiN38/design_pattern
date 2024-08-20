from unittest.mock import MagicMock, patch

import pytest

from src.structure.proxy.factory.image_proxy import ProxyImage
from src.structure.proxy.models.image import RealImage


@pytest.fixture
def mock_real_image():
    mock = MagicMock(spec=RealImage)
    mock.filename = "data/image_001.jpg"
    mock.image = MagicMock()
    mock.image.size = (4160, 6240)
    mock.image.format = "JPEG"
    mock.image.mode = "RGB"
    mock.image.info = {"dpi": (72, 72)}
    return mock


@pytest.fixture
def mock_real_image_class(mock_real_image):
    with patch(
        "src.structure.proxy.models.image.RealImage", return_value=mock_real_image
    ) as mock_class:
        yield mock_class


def test_proxy_image_display():
    proxy_image = ProxyImage("data/image_001.jpg")
    proxy_image.display()


def test_proxy_image_get_metadata(mock_real_image_class):
    proxy_image = ProxyImage("data/image_001.jpg")
    metadata = proxy_image.get_metadata()

    assert metadata == ("data/image_001.jpg", 4160, 6240)
