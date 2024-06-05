//Событие для появления бэкраунда при прокрутке
$(document).ready(function () {
	// Задаем след за событием прокрутки
	$(window).scroll(function () {
			// Если прокрутка больше чем 50px, добавляем класс
			if ($(this).scrollTop() > 50) {
					$('.navbar').addClass('navbar-scrolled');
			} else {
					// В противном случае удаляем класс
					$('.navbar').removeClass('navbar-scrolled');
			}
	});
});

document.addEventListener("DOMContentLoaded", function () {
	const deliverySelect = document.getElementById("id_requires_delivery");
	const deliveryAddressField = document.getElementById("deliveryAddressField");

	function toggleDeliveryAddress() {
		if (deliverySelect.value == "1") {
			deliveryAddressField.style.display = "block";
		} else {
			deliveryAddressField.style.display = "none";
		}
	}

	deliverySelect.addEventListener("change", toggleDeliveryAddress);
	toggleDeliveryAddress();
});