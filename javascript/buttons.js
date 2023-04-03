const navMenuBtn = document.querySelector('.mobile__nav-burger-btn'),
			navMenuBtnClose = document.querySelector('.mobile__nav-close'),
			navMenu = document.querySelector('.mobile__nav')
			
navMenuBtn.addEventListener('click', () => {
	event.preventDefault()
	navMenu.classList.add('show')
})
navMenuBtnClose.addEventListener('click', () => {
	event.preventDefault()
	navMenu.classList.remove('show')
})