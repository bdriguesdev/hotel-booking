<template>
    <svg :style="booking.review? {}: { cursor: 'pointer' }" @click="handleClick" xmlns="http://www.w3.org/2000/svg" width="25" height="23" viewBox="0 0 25 23" fill="none">
        <path :fill="color" d="M11.2544 -0.2004L8.42017 5.74726L2.07903 6.7041C0.941874 6.8748 0.486145 8.32578 1.3108 9.15684L5.89847 13.7838L4.8134 20.3199C4.61809 21.5014 5.82035 22.3863 6.82729 21.8338L12.5 18.7477L18.1728 21.8338C19.1797 22.3818 20.382 21.5014 20.1867 20.3199L19.1016 13.7838L23.6893 9.15684C24.5139 8.32578 24.0582 6.8748 22.921 6.7041L16.5799 5.74726L13.7457 -0.2004C13.2379 -1.26056 11.7665 -1.27403 11.2544 -0.2004Z"/>
    </svg>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    name: 'ReviewStarIcon',
    props: [
        'color',
        'num'
    ],
    methods: {
        handleClick() {
            const svgPaths = document.querySelectorAll('.booking__reviews__rating svg path');
            for(let x = 0; x < this.num; x++) {
                svgPaths[x].style.fill = '#FFDD65';
            }
            for(let x = this.num; x < 5; x++) {
                svgPaths[x].style.fill = '#FEF5D7';
            }
            this.$emit('reviewValue', this.num);
        }
    },
    computed: {
        ...mapGetters([
            'booking'
        ])
    }
}
</script>

<style>
</style>