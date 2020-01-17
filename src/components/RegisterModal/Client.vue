<template>
    <form class="register__form" @submit.prevent="createClient">
        <label for="firstName">
            First name
            <input type="text" v-model="firstName"/>
        </label>
        <label for="secondName">
            Last name
            <input type="text" v-model="lastName"/>
        </label>
        <label for="email">
            Email
            <input type="email" v-model="email"/>
        </label> 
        <!-- for date i have more options in the input -->
        <label for="birthday">
            Birthday
            <input type="date" v-model="birthday"/>
        </label>
        <label for="secondName">
            State
            <input type="text" v-model="state"/>
        </label>
        <label for="secondName">
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
    name: 'Client',
    data() {
        return {
            isRegisterButtonAnimationInProgress: false,
            firstName: null,
            lastName: null,
            email: null,
            birthday: null,
            state: null,
            city: null,
            password: null,
            repeatedPassword: null
        }
    },
    methods: {
        createClient() {
            this.$store.dispatch('createClient', {
                firstName: this.firstName,
                lastName: this.lastName,
                birthday: this.birthday,
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