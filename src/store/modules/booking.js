import store from '../index';

const state = {
    bookings: null,
    booking: null,
    bookingId: null,
    bookingLoading: null,
    bookingStart: null,
    bookingEnd: null,
    reviews: null
};

const mutations = {
    SET_BOOKING_LOADING(state, loadingBoolean) {
        state.bookingLoading = loadingBoolean;
    },
    SET_BOOKING_START(state, date) {
        state.bookingStart = date;
    },
    SET_BOOKING_END(state, date) {
        state.bookingEnd = date;
    },
    SET_BOOKINGS(state, bookings) {
        state.bookings = bookings;
    },
    SET_BOOKING(state, booking) {
        state.booking = booking;
    },
    SET_BOOKING_ID(state, bookingId) {
        state.bookingId = bookingId;
    },
    SET_REVIEWS(state, reviews) {
        state.reviews = reviews;
    }
};

const actions = {
    changeReviews({ commit }, reviews) {
        commit('SET_REVIEWS', reviews);
    },
    changeBooking({ commit }, booking) {
        commit('SET_BOOKING', booking);
    },
    changeBookingId({ commit }, bookingId) {
        commit('SET_BOOKING_ID', bookingId);
    },
    changeBookingLoading({ commit }, loadingBoolean) {
         commit('SET_BOOKING_LOADING', loadingBoolean);
    },
    changeBookingStart({ commit }, date) {
        commit('SET_BOOKING_START', date);
    },
    changeBookingEnd({ commit }, date) {
        commit('SET_BOOKING_END', date);
    },
    createBooking({ commit }, { roomId, coupon }) {
        let requestBody = {
            roomId,
            startAt: store.getters.bookingStart.toUTCString(),
            endAt: store.getters.bookingEnd.toUTCString(),
            coupon
        };

        return fetch('http://127.0.0.1:8000/api/booking/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Token': store.getters.token,
                'User-Type': store.getters.userType
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            //eslint-disable-next-line
            console.log(data);
            commit('SET_BOOKING', data);
            commit('SET_BOOKING_LOADING', false);
        }).catch(err => {
            //eslint-disable-next-line
            console.log(err);
        });
    },
    getBookings({ commit }, { startAt, endAt, city, state, minPrice, maxPrice }) {
        let requestBody = {
            startAtSearch: startAt? 'True': 'False',
            startAt,
            endAtSearch: endAt? 'True': 'False',
            endAt,
            citySearch: city? 'True': 'False',
            stateSearch: state? 'True': 'False',
            minPriceSearch: minPrice? 'True': 'False',
            minPrice,
            maxPriceSearch: maxPrice? 'True': 'False',
            maxPrice,
            reviewSearch: 'False',
            clientSearch: 'True'
        };

        return fetch('http://127.0.0.1:8000/api/booking/user/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Token': store.getters.token,
                'User-Type': store.getters.userType
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_BOOKINGS', data);
            commit('SET_BOOKING_LOADING', false);
        }).catch(err => {
            //eslint-disable-next-line
            console.log(err);
        })
    },
    createReview(a, { description, value }) {
        let requestBody = {
            value,
            description,
            roomId: store.getters.booking.room.id,
            bookingId: store.getters.booking.id
        };

        return fetch('http://127.0.0.1:8000/api/review/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Token': store.getters.token,
                'User-Type': store.getters.userType
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            //eslint-disable-next-line
            console.log(data);
            // commit('SET_BOOKING', data);
        }).catch(err => {
            //eslint-disable-next-line
            console.log(err);
        })
    },
    getRoomReviews({ commit }) {
        let requestBody = {
            roomId: store.getters.room.id
        };

        return fetch('http://127.0.0.1:8000/api/review/room/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_REVIEWS', data);
            commit('SET_BOOKING_LOADING', false);
        }).catch(err => {
            //eslint-disable-next-line
            console.log(err);
        })
    },
    getReviewsAllRoomsFromHotel({ commit }) {
        let requestBody = {
            hotelId: store.getters.hotelId
        };

        return fetch('http://127.0.0.1:8000/api/review/hotel/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_REVIEWS', data);
            commit('SET_BOOKING_LOADING', false);
        }).catch(err => {   
            //eslint-disable-next-line
            console.log(err);
        })
    },
    getRoomBookingsPerMonth({ commit }, { roomId, bookingsYear, bookingsMonth }) {
        let requestBody = { 
            roomId,
            bookingsMonth: bookingsMonth + 1,
            bookingsYear 
        };

        return fetch('http://127.0.0.1:8000/api/booking/month/', {
            'method': 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_BOOKINGS', data);
        }).catch(err => {
            //eslint-disable-next-line
            console.log(err);
        })
    },
    getHotelBookings({ commit }, { hotelId, month, year }) {
        let requestBody = {
            hotelId,
            month: month + 1,
            year
        };

        return fetch('http://127.0.0.1:8000/api/booking/hotel/', {
            'method': 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Token': store.getters.token,
                'User-Type': store.getters.userType
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_BOOKINGS', data);
        }).catch(err => {
            //eslint-disable-next-line
            console.log(err);
        })
    },
    getRoomBookingsWithDetails({ commit }, { roomId, month, year }) {
        let requestBody = {
            roomId,
            month: month + 1,
            year
        };
 
        return fetch('http://127.0.0.1:8000/api/booking/room/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Token': store.getters.token,
                'User-Type': store.getters.userType
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json()
        }).then(data => {
            commit('SET_BOOKINGS', data);
        }).catch(err => {
            //eslint-disable-next-line
            console.log(err);
        })
    }
};

const getters = {
    bookingLoading: state => state.bookingLoading,
    bookings: state => state.bookings,
    booking: state => state.booking,
    bookingStart: state => state.bookingStart,
    bookingEnd: state => state.bookingEnd,
    bookingId: state => state.bookingId,
    reviews: state => state.reviews
};

const bookingModule = {
    state,
    mutations,
    actions,
    getters
};

export default bookingModule;