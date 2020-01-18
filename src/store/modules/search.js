const state = {
    roomSearch: null,
    hotelSearch: null,
    searchLoading: null,
    searchType: null,
    searchAmount: null
};

const mutations = {
    SET_ROOM_SEARCH(state, room) {
        state.roomSearch = room;
    },
    SET_HOTEL_SEARCH(state, hotel) {
        state.hotelSearch = hotel;
    },
    SET_SEARCH_LOADING(state, loadingBoolean) {
        state.searchLoading = loadingBoolean;
    },
    SET_SEARCH_TYPE(state, type) {
        state.searchType = type;
    },
    SEARCH_AMOUNT(state, amount) {
        state.searchAmount = amount;
    }
};

const actions = {
    changeSearchLoading({ commit }, loadingBoolean) {
        commit('SET_SEARCH_LOADING', loadingBoolean);
    },
    changeSearchType({ commit }, type) {
        commit('SET_SEARCH_TYPE', type);
    },
    searchRooms({ commit }, { name, city, state, minPrice, maxPrice }) {
        let requestBody = {
            nameSearch: name !== ""? "True": "False",
            name,
            citySearch: city !== ""? "True": "False",
            city,
            stateSearch: state !== ""? "True": "False",
            state,
            priceRange: minPrice >= 1 || maxPrice >= 1 ? "True": "False",
            minPrice: minPrice !== ""? minPrice: -1,
            maxPrice: maxPrice !== ""? maxPrice: -1,
            hotelIdSearch: "False",
            hotelNameSearch: "False"
        };

        return fetch('http://127.0.0.1:8000/api/room/search/all/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody),
        }).then(data => {
            return data.json();
        }).then(data => {
            if(data.error) {
                commit('SET_ROOM_SEARCH', null);
                commit('SET_SEARCH_TYPE', null);
                commit('SET_SEARCH_LOADING', null);
                commit('SEARCH_AMOUNT', null); 
            } else {
                commit('SET_ROOM_SEARCH', data);
                commit('SET_SEARCH_TYPE', 'room');
                commit('SET_SEARCH_LOADING', false);
                commit('SEARCH_AMOUNT', data.length);
            }
        }).catch(() => {
            commit('SET_ROOM_SEARCH', null);
            commit('SET_SEARCH_TYPE', null);
            commit('SET_SEARCH_LOADING', null);
            commit('SEARCH_AMOUNT', null); 
        });
    },
    searchHotels({ commit }, { name, city, state }) {
        let requestBody = {
            nameSearch: name !== ""? "True": "False",
            name,
            citySearch: city !== ""? "True": "False",
            city,
            stateSearch: state !== ""? "True": "False",
            state,
            businessSearch: "False"
        };

        return fetch('http://127.0.0.1:8000/api/hotel/search/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody),
        }).then(data => {
            return data.json();
        }).then(data => {
            if(data.error) {
                commit('SET_HOTEL_SEARCH', null);
                commit('SET_SEARCH_TYPE', null);
                commit('SET_SEARCH_LOADING', null);
                commit('SEARCH_AMOUNT', null);
            } else {
                commit('SET_HOTEL_SEARCH', data);
                commit('SET_SEARCH_TYPE', 'hotel');
                commit('SET_SEARCH_LOADING', false);
                commit('SEARCH_AMOUNT', data.length);
            }
        }).catch(() => {
            commit('SET_HOTEL_SEARCH', null);
            commit('SET_SEARCH_TYPE', null);
            commit('SET_SEARCH_LOADING', null);
            commit('SEARCH_AMOUNT', null);
        });
    }
};

const getters = {
    roomSearch: state => state.roomSearch,
    hotelSearch: state => state.hotelSearch,
    searchLoading: state => state.searchLoading,
    searchType: state => state.searchType,
    searchAmount: state => state.searchAmount
};

const searchModules = {
    state,
    mutations,
    actions,
    getters
};

export default searchModules;