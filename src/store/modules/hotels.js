import store from '../index';

const state = {
    hotel: null,
    hotels: null,
    hotelId: null,
    message: null,
    hotelLoading: false
};

const mutations = {
    SET_HOTEL(state, hotel) {
        state.hotel = hotel;
    },
    SET_HOTELS(state, hotels) {
        state.hotels = hotels;
    },
    SET_HOTEL_ID(state, hotelId) {
        state.hotelId = hotelId;
    },
    SET_HOTEL_LOADING(state, loading) {
        state.hotelLoading = loading;
    }
};

const actions = {
    changeLoading({ commit }, value) {
        commit('SET_HOTEL_LOADING', value);
    },
    changeHotel({ commit }, hotel) {
        commit('SET_HOTEL', hotel);
    },
    createHotel({ commit, dispatch }, { hotelName, state, city, street, number, complement, description }) {
        let requestBody = {
            hotelName,
            state,
            city,
            street,
            number,
            complement,
            description
        };

        return fetch('http://127.0.0.1:8000/api/hotel/create/', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "Token": store.getters.token,
                "User-Type": "Business"
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_ROOM', data.hotel);
            dispatch('getAllUserHotels');
        }).catch(err => {
            // eslint-disable-next-line
            console.log(err);
        });
    },
    changeHotelPhoto({ getters }, { photo }) {
        const formData = new FormData();
        formData.append('photo', photo);
        formData.append('hotelId', getters.hotel.id);
        formData.append('priority', 1);

        return fetch('http://127.0.0.1:8000/api/hotel/image_upload/', {
            method: 'PUT',
            headers: {
                'Token': getters.token,
                'User-Type': getters.userType 
            },
            body: formData
        }).then(data => {
            return data.json();
        }).then(() => {
            return;
        }).catch(err => {
            //eslint-disable-next-line
            console.log(err);
        });
    },
    editHotel({ commit }) {
        let requestBody = {};

        return fetch('link', {
            method: 'UPDATE',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_HOTEL', data.hotel);
        }).catch(err => {
            // eslint-disable-next-line
            console.log(err);
        });
    },
    deleteHotel({ commit }) {
        let requestBody = {};

        return fetch('link', {
            method: 'DELETE',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_HOTEL', data.hotel);
        }).catch(err => {
            // eslint-disable-next-line
            console.log(err);
        });
    },
    getMostPopularHotels({ commit }) {

        return fetch('http://127.0.0.1:8000/api/hotel/popular/', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json"
            }
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_HOTELS', data);
            commit('SET_HOTEL_LOADING', false);
        }).catch(err => {
            // eslint-disable-next-line
            console.log(err);
        });
    },
    getHotel({ commit, dispatch }, { hotelId }) {
        let requestBody = { hotelId };

        commit('SET_HOTEL_ID', hotelId);
        return fetch('http://127.0.0.1:8000/api/hotel/details/', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_HOTEL', data);
            commit('SET_HOTEL_LOADING', false);
            dispatch('getReviewsAllRoomsFromHotel');
        }).catch(err => {
            // eslint-disable-next-line
            console.log(err);
        });
    },
    getAllUserHotels({ commit }) {

        return fetch('http://127.0.0.1:8000/api/hotel/all/', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "Token": store.getters.token,
                "User-Type": "Business"
            }
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_HOTELS', data);
        }).catch(err => {
            // eslint-disable-next-line
            console.log(err);
        });
    },
    setHotelId({ commit }, { id }) {
        commit('SET_HOTEL_ID', id);
    },
    filterHotels({ commit }, { citySearch, city, stateSearch, state, nameSearch, name, businessSearch, businessId }) {
        let requestBody = {
            citySearch,
            city,
            stateSearch,
            state,
            nameSearch,
            name,
            businessSearch,
            businessId
        };

        return fetch('http://127.0.0.1:8000/api/hotel/search/', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_HOTELS', data);
        }).catch(err => {
            //eslint-disable-next-line
            console.log(err);
        });
    }
};

const getters = {
    hotel: state => state.hotel,
    hotels: state => state.hotels,
    hotelId: state => state.hotelId,
    hotelLoading: state => state.hotelLoading
};

const hotelsModule = {
    state,
    mutations,
    actions,
    getters
};

export default hotelsModule;