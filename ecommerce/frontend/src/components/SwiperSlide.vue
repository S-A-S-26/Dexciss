<template>

    <swiper
      :pagination="{
        dynamicBullets: true,
      }"
      :modules="modules"
      class="mySwiper"
    >
      <swiper-slide v-for="item in dat" :key="item.id">
        <div class="innerSlideContainer">
          <SlideTemplate :data="item" />
        </div>
      </swiper-slide>
      <!-- <swiper-slide><div class="innerSlideContainer">Slide 2</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 3</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 4</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 5</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 6</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 7</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 8</div></swiper-slide>
      <swiper-slide><div class="innerSlideContainer">Slide 9</div></swiper-slide> -->
    </swiper>

    <!-- <li v-for="item in dat" :key="item.id">
        {{ item }}
        <SlideTemplate :data="item" />
    </li> -->
    <!-- {{ dat}} -->
    <!-- <SlideTemplate :data="dat[0]" /> -->
</template>

<script>
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';
import SlideTemplate from './SlideTemplate.vue'

import 'swiper/css';

import 'swiper/css/pagination';



// import required modules
import { Pagination } from 'swiper/modules';

export default {
    props:  {
      dat:Array
    },

    mounted(){
      console.log(this.dat)
    },


    components: {
    Swiper,
    SwiperSlide,
    SlideTemplate,
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
  min-width:400px;
  max-width:1000px;
  /* height: auto; */
  margin:0;
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
    border:solid red;
    /* height: 500px;
    width: 500px; */
    /* display: grid;
    place-items: center; */
    
}



</style>
