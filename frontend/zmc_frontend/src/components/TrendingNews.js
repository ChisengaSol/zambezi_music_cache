import '../styles/TrendingNews.css';
const TrendingNews = () => {
    let slides = document.getElementsByClassName("slider__slide");
    let navlinks = document.getElementsByClassName("slider__navlink");
    let currentSlide = 0;

    const el = document.getElementById("nav-button--next");
    if(el){
        el.addEventListener("click", () => {
            changeSlide(currentSlide + 1)
        });
    }
    
    const el2 = document.getElementById("nav-button--prev");
    if(el2){
        el2.addEventListener("click", () => {
            changeSlide(currentSlide - 1)
        });
    }

    function changeSlide(moveTo) {
        if (moveTo >= slides.length) {moveTo = 0;}
        if (moveTo < 0) {moveTo = slides.length - 1;}
        
        slides[currentSlide].classList.toggle("active");
        navlinks[currentSlide].classList.toggle("active");
        slides[moveTo].classList.toggle("active");
        navlinks[moveTo].classList.toggle("active");
        
        currentSlide = moveTo;
    }

    document.querySelectorAll('.slider__navlink').forEach((bullet, bulletIndex) => {
        bullet.addEventListener('click', () => {
            if (currentSlide !== bulletIndex) {
                changeSlide(bulletIndex);
            }
        })
    })

    return ( 
        <div className="container">
        <div className="slider">
          <div className="slider__slides">
            <div className="slider__slide active">
               <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Shakuzoji_Kuginuki_Jizo-3586.jpg/800px-Shakuzoji_Kuginuki_Jizo-3586.jpg" alt="A rooftop in Japan" />
            </div>
            <div className="slider__slide">
              <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Stirling_Castle_Main_Gate.jpg/800px-Stirling_Castle_Main_Gate.jpg" alt="A castle in Scotland" />
            </div>
            <div className="slider__slide">
              <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Xiaoqingshan_Farm_Product_Market%2C_Puding_County%2C_Guizhou%2C_China2.jpg/800px-Xiaoqingshan_Farm_Product_Market%2C_Puding_County%2C_Guizhou%2C_China2.jpg" alt="A street market in China" />
            </div>
            <div className="slider__slide">
              <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Patung_Buddha_Tidur_Trowulan.jpg/800px-Patung_Buddha_Tidur_Trowulan.jpg" alt="A statue of the Buddha in Thailand" />
            </div>
          </div>
          <div id="nav-button--prev" className="slider__nav-button"></div>
          <div id="nav-button--next" className="slider__nav-button"></div>
          <div className="slider__nav">
            <div className="slider__navlink active"></div>
            <div className="slider__navlink"></div>
            <div className="slider__navlink"></div>
            <div className="slider__navlink"></div>
          </div>
        </div>
      </div>
     );
}
 
export default TrendingNews;