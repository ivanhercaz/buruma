document.addEventListener("DOMContentLoaded", () => {
	// Burger items
	const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll(".navbar-burger"), 0);

	if ($navbarBurgers.length > 0) {
		// Click event on each item
		$navbarBurgers.forEach( item => {
			item.addEventListener("click", () => {
				// Get "data-target" attribute
				const target = item.dataset.target;
				const $target = document.getElementById(target);

				// Toggle "is active
				item.classList.toggle("is-active");
				$target.classList.toggle("is-active");
			});
		});
	}
});
