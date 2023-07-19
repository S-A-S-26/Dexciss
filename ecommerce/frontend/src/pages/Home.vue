<template>
    <div class="HomeContainer">
        <!-- <SwiperSlide :dat="slider_list" /> -->
        <!-- <HeroContainer/> -->
        <!-- <SlideTemplate :data="obj" /> -->
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import SwiperSlide from '../components/SwiperSlide.vue'
    import {slider_list} from '../data/sliderData';
    import SlideTemplate from '../components/SlideTemplate.vue';
    import HeroContainer from '../components/HeroContainer.vue';
    const obj=ref(slider_list[0])
</script>

<style scoped>

</style>