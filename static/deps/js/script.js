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

/*-------------------
		Radio Btn
	--------------------- */
/*	$(".product__color__select label, .shop__sidebar__size label, .product__details__option__size label").on('click', function () {
		$(".product__color__select label, .shop__sidebar__size label, .product__details__option__size label").removeClass('active');
		$(this).addClass('active');
});*/

/*-------------------
		Price sidebar
	--------------------- */
	