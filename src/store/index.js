import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';

import authModule from './modules/auth';
import hotelsModule from './modules/hotels';
import roomsModule from './modules/rooms';
import searchModule from './modules/search';
import bookingModule from './modules/booking';
import errorModule from './modules/error';

Vue.use(Vuex);
Vue.use(VueRouter);

export default new Vuex.Store({
    modules: {
        authModule,
        hotelsModule,
        roomsModule,
        searchModule,
        bookingModule,
        errorModule
    }
});