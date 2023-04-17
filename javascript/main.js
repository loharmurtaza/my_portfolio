//section__my-recent-projects slider

$('.section__my-recent-projects__grid').slick({
	arrows: true,
	dots: true,
	autoplay: true,
	infinite: true,
	slidesToShow: 3,
  slidesToScroll: 1,
  autoplaySpeed: 4000,
	responsive: [
    {
      breakpoint: 768,
      settings: {
      slidesToShow: 1,
      centerMode: false, /* set centerMode to false to show complete slide instead of 3 */
      slidesToScroll: 1
      }
    }
	]
})
$('.section__feedback__grid').slick({
	arrows: false,
	dots: true,
	autoplay: true,
	infinite: true,
	slidesToShow: 2,
  slidesToScroll: 1,
  autoplaySpeed: 4000,
	responsive: [
    {
      breakpoint: 768,
      settings: {
      slidesToShow: 1,
      centerMode: false, /* set centerMode to false to show complete slide instead of 3 */
      slidesToScroll: 1
      }
    }
	]
})

// running string

const runningString = document.getElementById('running__string')
const runningLine = 'Ui & Ux Designer'
const speed = 120
let i = 0
console.log(runningString.innerHTML)

function run() {
	if (i++ < runningLine.length) {
		runningString.innerHTML = runningLine.substring(0, i) + '|'
	}
	else {
		runningString.innerHTML = ''
		i = 0
	}
	done = setTimeout('run()', speed)
}

run()
