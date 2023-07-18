<template>
    <swiper
      :pagination="{
        dynamicBullets: true,
      }"
      :modules="modules"
      class="mySwiper"
    >
      <swiper-slide><div class="innerSlideContainer">Slide 1</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 2</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 3</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 4</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 5</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 6</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 7</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 8</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 9</div></swiper-slide>
    </swiper>
</template>
<script>
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';

// Import Swiper styles
import 'swiper/css';

import 'swiper/css/pagination';



// import required modules
import { Pagination } from 'swiper/modules';

export default {
    components: {
    Swiper,
    SwiperSlide,
    },
    setup() {
    return {
        modules: [Pagination],
    };
    },
};
</script>

<style scoped>
.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;

  /* Center slide text vertically */
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.innerSlideContainer{
    border:solid;
    height: 500px;
    width: 500px;
    display: grid;
    place-items: center;
    
}
</style>
