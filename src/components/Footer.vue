<template>
    <footer class="footer">
        <nav class="footer-nav">
            <ul>
                <li @click="changePage('/')">home</li>
                <div class="line"></div>
                <li @click="searchRooms">rooms</li>
                <div class="line"></div>
                <li @click="hotelsSearch">hotels</li>
            </ul>
        </nav>
        <div class="credits">
            <svg width="52" height="35" viewBox="0 0 52 35" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="17.4571" cy="17.4571" r="17.4571" fill="white"/>
                <circle cx="34.5429" cy="17.4571" r="17.4571" fill="#FF1E1E"/>
            </svg>
            <span class="text">Roboto - 2020</span>
        </div>
    </footer>
</template>

<script>
export default {
    name: 'Footer',
    methods: {
        changePage(path) {
            if(this.$route.path === path) {
                window.scrollTo(0,0);
                this.$router.push({ path: '/abcd' });
                setTimeout(() => {
                    this.$router.push({ path });
                }, 1);
            } else {
                window.scrollTo(0,0);
                this.$router.push({ path });
            }
        },
        searchRooms() {
            const args = {
                name: "",
                minPrice: "",
                maxPrice: "",
                state: "",
                city: ""
            };
            this.$store.dispatch('searchRooms', args).then(() => {
                window.scrollTo(0,0);
                const path = '/search/';
                if(this.$route.path !== path) this.$router.push({ path: '/search/' });
                else {
                    this.$router.push({ path: '/abcd' });
                    setTimeout(() => {
                        this.$router.push({ path });
                    }, 1);
                }
            });
        },
        hotelsSearch() {
            const args = {
                name: "",
                state: "",
                city: ""
            };
            this.$store.dispatch('searchHotels', args).then(() => {
                window.scrollTo(0,0);
                const path = '/search/';
                if(this.$route.path !== path) this.$router.push({ path });
                else {
                    this.$router.push({ path: '/abcd' });
                    setTimeout(() => {
                        this.$router.push({ path });
                    }, 1);
                }
            });
        }
    }
}
</script>

<style lang='scss'>
     @import '../scss/variables.scss';
     @import '../scss/mixins.scss';

    .footer {
        max-width: 1920px;
        margin: 0 auto;
        padding: 50px 0 40px 0;
        margin-top: 100px;
        background-color: black;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        @include medium-phone {
            margin-top: 350px;
        }
        @include small-phone {
            margin-top: 450px;
        }
        @include micro-phone {
            margin-top: 550px;
        }

        .footer-nav {

            ul {
                list-style: none;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;

                a {
                    text-decoration: none;
                }
                
                li {
                    font-size: 1.063rem;
                    font-weight: 400;
                    color: $primary-color;
                    margin: 0 15px;
                    cursor: pointer;
                    transition: 200ms ease-in-out;
                }

                li:hover {
                    color: $secondary-color-one;
                }

                .line {
                    width: 10px;
                    height: 1px;
                    background-color: $primary-color;
                }
            }
        }

        .credits {
            margin-top: 30px;
            display: flex;
            align-items: center;

            .text {
                font-size: 1.063rem;
                color: $primary-color;
                font-weight: 400;
                margin-left: 10px;
            }
        }
    }
</style>