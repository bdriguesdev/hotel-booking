import store from '../index';

const state = {
    rooms: null,
    hotelRooms: null,
    room: null,
    roomLoading: false
};

const mutations = {
    SET_ROOM(state, room) {
        state.room = room;
    },
    SET_ROOMS(state, rooms) {
        state.rooms = rooms;
    },
    SET_HOTEL_ROOMS(state, hotelRooms) {
        state.hotelRooms = hotelRooms;
    },
    SET_ROOM_LOADING(state, loading) {
        state.roomLoading = loading;
    },
    SET_ROOMS_SEARCH(state, rooms) {
        state.roomsSearch = rooms;
    }
};

const actions = {
    changeRoomLoading({ commit }, value) {
        commit('SET_ROOM_LOADING', value);
    },
    changeRoom({ commit }, room) {
        commit('SET_ROOM', room);
    },
    changeRoomPhoto({ commit, getters, dispatch }, { photo }) {
        const formData = new FormData();
        formData.append('photo', photo);
        formData.append('roomId', getters.room.id);
        formData.append('priority', 1);

        return fetch('http://127.0.0.1:8000/api/room/image_upload/', {
            method: 'PUT',
            headers: {
                'Token': getters.token,
                'User-Type': getters.userType 
            },
            body: formData
        }).then(data => {
            return data.json();
        }).then(data => {
            if(data.error) {
                dispatch('changeError', data.error);
            } else {
                const hotelRooms = getters.hotelRooms;
                const roomId = getters.room.id;
                hotelRooms.forEach(room => {
                    if(room.id === roomId) {
                        if(!room.photos[0]) {
                            room.photos[0] = data;
                        } else {
                            room.photos.forEach((photo, index) => {
                                if(photo.priority === 1) {
                                    room.photos[index] = data;
                                }
                            })
                        }
                    }
                });
                commit('SET_HOTEL_ROOMS', hotelRooms);
            }
        }).catch(() => {
            dispatch('changeError', 'An error has been occurred.');
        });
    },
    createRoom({ commit, dispatch }, { name, description, price}) {
        let requestBody = {
            name,
            description,
            price,
            hotelId: store.getters.hotelId
        };

        return fetch('http://127.0.0.1:8000/api/room/create/', {
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
            if(data.error) {
                dispatch('changeError', data.error);
            } else {
                commit('SET_ROOM', data.room);
                dispatch('getAllRoomsFromOneHotel');
            }
        }).catch(() => {
            dispatch('changeError', 'An error has been occurred');
        });
    },
    editRoom({ commit }) {
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
           commit('SET_ROOM', data.room); 
        }).catch(err => {
            // eslint-disable-next-line
            console.log(err);
        });
    },
    deleteRoom({ commit }) {
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
            commit('SET_ROOM', data.room);
        }).catch(err => {
            // eslint-disable-next-line
            console.log(err);
        });
    },
    getMostPopularRooms({ commit }) {

        return fetch('http://127.0.0.1:8000/api/room/popular/', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json"
            }
        }).then(data => {
            return data.json();
        }).then(data => {
            if(data.error) {
                commit('SET_ROOMS', null);
            } else {
                commit('SET_ROOMS', data);
            }
            commit('SET_ROOM_LOADING', false);
        }).catch(() => {
            commit('SET_ROOMS', null);
        });
    },
    getRoom({ commit, dispatch }, { roomId }) {
        let requestBody = { roomId };

        return fetch('http://127.0.0.1:8000/api/room/details/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            if(data.error) {
                commit('SET_ROOM', null);
            } else {
                commit('SET_ROOM', data);
                dispatch('getRoomReviews');
            }
            commit('SET_ROOM_LOADING', false);
            
        }).catch(() => {
            commit('SET_ROOM', null);
        });
    },
    getAllRoomsFromOneHotel({ commit }) {
        let requestBody = { hotelId: store.getters.hotelId };

        return fetch('http://127.0.0.1:8000/api/room/hotel/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Token': store.getters.token,
                'User-Type': 'Business'
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            if(data.error) {
                commit('SET_HOTEL_ROOMS', null);
            } else {
                commit('SET_HOTEL_ROOMS', data);
            }
            commit('SET_ROOM_LOADING', false);
        }).catch(() => {
            commit('SET_HOTEL_ROOMS', null);
        });
    },
    filterHotelRooms({ commit }, { nameSearch, name, citySearch, city, stateSearch, state }) {
        let requestBody = {
            priceRange: "False",
            hotelIdSearch: "True",
            hotelId: store.getters.hotelId,
            hotelNameSearch: "False",
            nameSearch,
            name,
            stateSearch,
            state,
            citySearch,
            city
        };

        return fetch('http://127.0.0.1:8000/api/room/search/all/', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            if(data.error) {
                commit('SET_HOTEL_ROOMS', null);
            } else {
                commit('SET_HOTEL_ROOMS', data);
            }
            commit('SET_ROOM_LOADING', false);
        }).catch(() => {
            commit('SET_HOTEL_ROOMS', null);
        })
    }
};

const getters = {
    room: state => state.room,
    rooms: state => state.rooms,
    hotelRooms: state => state.hotelRooms,
    roomLoading: state => state.roomLoading
};

const roomsModule = {
    state,
    mutations,
    actions,
    getters
};

export default roomsModule;