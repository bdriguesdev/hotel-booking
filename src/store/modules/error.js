const state = {
    error: null
};

const mutations = {
    SET_ERROR(state, value) {
        state.error = value;
    }
};

const actions = {
    changeError({ commit }, value) {
        commit('SET_ERROR', value);
    }
}

const getters = {
    error: state => state.error
}

const errorModule = {
    state,
    mutations,
    actions,
    getters
};

export default errorModule;