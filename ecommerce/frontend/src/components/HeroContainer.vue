<template>
    <div class="heroContainer">
        
        <div class="flexContainer1">
            0.1
            <SwiperSlide :dat="slider_list"/>
            
        </div>

        <div class="flexContainer2">
            <div class="hero2Wrapper">
                1.1
                <!-- <SlideTemplate :data="hero2Data"/> -->
            </div>
            <div class="hero3Wrapper">
                1.2
                <!-- <SlideTemplate :data="hero3Data"/> -->
            </div>
        </div>

    </div>
</template>

<script setup>
    import SlideTemplate from './SlideTemplate.vue';
    import {hero2Data} from '../data/Hero2Data.js'
    import {hero3Data} from '../data/Hero3Data.js'
    import {slider_list} from '../data/sliderData';
    import SwiperSlide from '../components/SwiperSlide.vue'
</script>

<style scoped>
    .heroContainer{
        border:solid blue;
        display: flex;
    }
    
    .flexContainer1{
        border:solid red;
        flex-grow: 1;
    }
    .flexContainer2{
        border:solid orange;
        flex-grow: 0.5;
    }
    .hero2Wrapper,.hero3Wrapper{
        border:solid;
    }

</style>