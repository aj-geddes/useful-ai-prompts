# Python Mocking with unittest.mock

## Python Mocking with unittest.mock

```python
# services/order_service.py
from typing import Optional
from repositories.order_repository import OrderRepository
from services.payment_service import PaymentService
from services.notification_service import NotificationService

class OrderService:
    def __init__(
        self,
        order_repository: OrderRepository,
        payment_service: PaymentService,
        notification_service: NotificationService
    ):
        self.order_repository = order_repository
        self.payment_service = payment_service
        self.notification_service = notification_service

    def create_order(self, user_id: str, items: list) -> Order:
        """Create and process a new order."""
        order = self.order_repository.create({
            'user_id': user_id,
            'items': items,
            'status': 'pending'
        })

        try:
            payment = self.payment_service.process_payment(
                order.id,
                order.total
            )
            order.status = 'paid'
            order.payment_id = payment.id
            self.order_repository.update(order)

            self.notification_service.send_order_confirmation(
                order.user_id,
                order.id
            )
        except PaymentError as e:
            order.status = 'failed'
            self.order_repository.update(order)
            raise

        return order

# tests/test_order_service.py
import pytest
from unittest.mock import Mock, MagicMock, patch, call
from services.order_service import OrderService
from exceptions import PaymentError

class TestOrderService:
    @pytest.fixture
    def mock_dependencies(self):
        """Create mock dependencies."""
        return {
            'order_repository': Mock(),
            'payment_service': Mock(),
            'notification_service': Mock()
        }

    @pytest.fixture
    def order_service(self, mock_dependencies):
        """Create OrderService with mocked dependencies."""
        return OrderService(**mock_dependencies)

    def test_create_order_success(self, order_service, mock_dependencies):
        """Test successful order creation and payment."""
        # Arrange
        user_id = 'user-123'
        items = [{'product_id': 'p1', 'quantity': 2}]

        mock_order = Mock(
            id='order-123',
            total=99.99,
            status='pending',
            user_id=user_id
        )
        mock_payment = Mock(id='payment-123')

        mock_dependencies['order_repository'].create.return_value = mock_order
        mock_dependencies['payment_service'].process_payment.return_value = mock_payment

        # Act
        result = order_service.create_order(user_id, items)

        # Assert
        assert result.status == 'paid'
        assert result.payment_id == 'payment-123'

        mock_dependencies['order_repository'].create.assert_called_once_with({
            'user_id': user_id,
            'items': items,
            'status': 'pending'
        })

        mock_dependencies['payment_service'].process_payment.assert_called_once_with(
            'order-123',
            99.99
        )

        mock_dependencies['notification_service'].send_order_confirmation.assert_called_once_with(
            user_id,
            'order-123'
        )

        assert mock_dependencies['order_repository'].update.call_count == 1

    def test_create_order_payment_failure(self, order_service, mock_dependencies):
        """Test order creation when payment fails."""
        # Arrange
        mock_order = Mock(id='order-123', total=99.99, status='pending')
        mock_dependencies['order_repository'].create.return_value = mock_order
        mock_dependencies['payment_service'].process_payment.side_effect = PaymentError('Card declined')

        # Act & Assert
        with pytest.raises(PaymentError):
            order_service.create_order('user-123', [])

        # Verify order status was updated to failed
        assert mock_order.status == 'failed'
        mock_dependencies['order_repository'].update.assert_called()

        # Notification should not be sent
        mock_dependencies['notification_service'].send_order_confirmation.assert_not_called()

    @patch('services.order_service.datetime')
    def test_order_timestamp(self, mock_datetime, order_service, mock_dependencies):
        """Test order creation with mocked time."""
        # Arrange
        fixed_time = datetime(2024, 1, 1, 12, 0, 0)
        mock_datetime.now.return_value = fixed_time

        mock_order = Mock(id='order-123', created_at=fixed_time)
        mock_dependencies['order_repository'].create.return_value = mock_order

        # Act
        result = order_service.create_order('user-123', [])

        # Assert
        assert result.created_at == fixed_time
```
