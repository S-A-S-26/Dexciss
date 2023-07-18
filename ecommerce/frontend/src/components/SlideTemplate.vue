<template>
    <div class="imageContainer">
        <img alt="Slider img" :src="data.img" >
        <div class="slider_text">
            <h6>{{ data.text_1 }}</h6>
            <strong><h2>{{ data.text_2 }}</h2></strong>
            <h2>{{ data.text_3 }}</h2>
            <h2>{{ data.text_4 }}</h2>
            <h3>{{ data.text_5 }}</h3>
            <h3>{{ data.text_6 }}</h3>
            <span>{{ data.offer }}</span>
        </div>
    </div>
</template>

<script setup>

    const props=defineProps(
        {
            data:Object
        }
    )

</script>

<style scoped>
    img{
        object-fit: cover;
        /* position: absolute; */
    }
    .imageContainer{
        border:solid black;
        position: relative;
    }
    .slider_text{
        position: absolute;
        top: 40%;
        left: 25%;
    }
</style>