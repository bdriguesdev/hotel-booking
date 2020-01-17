import Vue from 'vue';
import VueRouter from 'vue-router';

import store from '../store/index.js'
import Home from '../pages/Home/Index.vue';
import Search from '../pages/Search/Index.vue';
import Room from '../pages/Room/Index.vue';
import Hotel from '../pages/Hotel/Index.vue';
import ClientBookings from '../pages/Client/Bookings/Index.vue';
import BusinessHotels from '../pages/Business/Hotels/Index.vue';
import HotelRooms from '../pages/Business/HotelRooms/Index.vue';

Vue.use(VueRouter)

/* eslint-disable no-console */
const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: Home
        },
        {
            path: '/search',
            component: Search
        },
        {
            path: '/room/:id',
            component: Room
        },
        {
            path: '/hotel/:id',
            component: Hotel
        },
        {
            path: '/client/bookings',
            component: ClientBookings,
            beforeEnter: (to, from, next) => {
                if (!store.getters.token || store.getters.userType !== 'Client') next('/');
                else next();
            }
        },
        {
            path: '/business/hotels',
            component: BusinessHotels,
            // beforeEnter: (to, from, next) => {
            //     if(!store.getters.token) next('/');
            //     else next();
            // }
        },
        {
            path: '/business/hotel/rooms',
            component: HotelRooms
        }
    ]
});

export default router;