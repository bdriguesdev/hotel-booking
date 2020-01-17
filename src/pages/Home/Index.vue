<template>
    <div class="index-content">
        <Header v-on="$listeners" />
        <main>
            <SectionOne v-on="$listeners" />
            <SectionTwo />
            <SectionThree />
            <SectionFour v-on="$listeners" />
        </main>
    </div>
</template>

<script>
import Header from '../../components/Header';
import SectionOne from './SectionOne';
import SectionTwo from './SectionTwo';
import SectionThree from './SectionThree';
import SectionFour from './SectionFour';

export default {
    name: 'Home',
    components: {
        Header,
        SectionOne,
        SectionTwo,
        SectionThree,
        SectionFour
    }
}
</script>

<style >
    /*$primary-color: #333;
    $secondary-color: #222;
    darkgray-color: #111; */
</style>