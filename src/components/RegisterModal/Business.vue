<template>
    <form class="register__form" @submit.prevent="createBusiness">
        <label for="businessName">
            Business name
            <input type="text" v-model="businessName"/>
        </label>
        <label for="email">
            Email
            <input type="email" v-model="email"/>
        </label> 
        <!-- for date i have more options in the input -->
        <label for="state">
            State
            <input type="text" v-model="state"/>
        </label>
        <label for="city">
            City
            <input type="text" v-model="city"/>
        </label>
        <label for="password">
            Password
            <input type="password" v-model="password"/>
        </label>
        <label for="repeatedPassword">
            Repeat the password
            <input type="password" v-model="repeatedPassword"/>
        </label>
        <button class="register__btn" v-on:click="btnAnimation" v-on:mouseenter="btnAnimation">
            Register now
            <div class="register__btn__container">
                <div class="register__btn--effect">
                    <img src="../../assets/Button_arrow_two.svg" alt="Register button icon" />
                    <img src="../../assets/Button_arrow_two.svg" alt="Register button icon" />
                </div>
            </div>
        </button>
    </form>
</template>

<script>
export default {
    name: 'Business',
    data() {
        return {
            isRegisterButtonAnimationInProgress: false,
            businessName: null,
            email: null,
            state: null,
            city: null,
            password: null,
            repeatedPassword: null
        }
    },
    methods: {
        createBusiness() {
            this.$store.dispatch('createBusiness', {
                name: this.businessName,
                email: this.email,
                state: this.state,
                city: this.city,
                password: this.password,
                repeatedPassword: this.repeatedPassword
            }).authModule;
        },
        btnAnimation() {
            if(!this.isBtnAnimationInProgress) {
                this.isBtnAnimationInProgress = true;
                const button = document.querySelector('.register__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isBtnAnimationInProgress = false;
                }, 500);
            }
        }
    }
}
</script>

<style lang='scss'>

</style>