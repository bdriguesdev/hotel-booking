<template>
    <div class="calendar__container__hotel__info">
        <div class="calendar__options">
            <div class="calendar__month">
                <img src="../../../assets/Mini_arrow_left.svg" alt="Month left arrow" @click="handleChangeClick('month', month - 1)">
                <span>{{ monthWord }}</span>
                <img src="../../../assets/Mini_arrow_right.svg" alt="Month right arrow" @click="handleChangeClick('month', month + 1)">
            </div>
            <div class="calendar__year">
                <img src="../../../assets/Mini_arrow_left.svg" alt="Year left arrow" @click="handleChangeClick('year', year - 1)">
                <span>{{ year }}</span>
                <img src="../../../assets/Mini_arrow_right.svg" alt="Year right arrow" @click="handleChangeClick('year', year + 1)">
            </div>
        </div>
        <div class="calendar__date">
            <div class="calendar__days-week">
                <span>Mon</span>
                <span>Tue</span>
                <span>Wed</span>
                <span>Thu</span>
                <span>Fri</span>
                <span>Sat</span>
                <span>Sun</span>
            </div>
            <div class="calendar__days">
                <ul v-for="(week, index) in calendarArray" :key="index" :id="`week${index}`">
                    <li v-for="(day, index) in week" :key="index" :class="`hotel${currentMonth}`" :id="`${day}`" >
                        {{ day }}
                    </li>
                </ul>
                <!-- container for each day -->
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
/* eslint-disable no-console */
export default {
    name: 'Calendar',
    data() {
        return {
            calendarArray: null,
            startAt: '--/-- --',
            endAt: '--/-- --',
            year: null,
            currentYear: null,
            month: null,
            currentMonth: null,
            monthWord: null
        }
    },
    mounted() {
        const date = new Date();
        this.currentYear = date.getFullYear();
        this.currentMonth = date.getMonth();
        this.calendarArray = this.changeCalendar(this.currentYear, this.currentMonth);
        this.year = this.currentYear;
        this.month = this.currentMonth;
        this.requestMonthBookings(this.currentMonth, this.currentYear);
    },
    methods: {
        requestMonthBookings(month=this.month, year=this.year) {
            const args = {
                hotelId: this.hotelId,
                month: month,
                year: year
            };
            this.$store.dispatch('getHotelBookings', args).then(() => {
                this.bookingsCalendarBackground();
            });
        },
        bookingsCalendarBackground() {
            const daysContainers = document.querySelectorAll(`.calendar__container__hotel__info .calendar__days ul .hotel${this.currentMonth}`);
            daysContainers.forEach(day => {
                day.style.color = '#626262';
            });
            this.bookings.forEach(booking => {
                const startDateArray = booking.start.split('-');
                const startDay = startDateArray[2].split('T')[0];
                const startMonth = startDateArray[1];
                const startYear = startDateArray[0];
                const endDateArray = booking.end.split('-');
                const endDay = endDateArray[2].split('T')[0];
                const endMonth = endDateArray[1];
                const endYear = endDateArray[0];
                
                if((startMonth == (this.month + 1) && startYear == this.year) || (endMonth == (this.month + 1) && endYear == this.year)) {
                    daysContainers.forEach(day => {
                        if(day.id >= startDay && day.id <= endDay) {
                            day.style.color = '#FF1E1E';
                        } 
                    });
                }
            });
        },
        handleChangeClick(type, newValue) {
            if(type === 'month') {
                if(newValue < 0 && this.currentYear - 1 !== this.year - 1) {
                    this.calendarArray = this.changeCalendar(this.year - 1, 11);
                    this.requestMonthBookings();
                } else if(newValue > 11 && this.year + 1 !== this.currentYear + 2) {
                    this.calendarArray = this.changeCalendar(this.year + 1, 0);
                    this.requestMonthBookings();
                } else if(newValue >= 0 && newValue <= 11) {
                    this.calendarArray = this.changeCalendar(this.year, newValue);
                    this.requestMonthBookings();
                }
            } else if(newValue <= this.currentYear + 1 && newValue && newValue >= this.currentYear) {
                this.calendarArray = this.changeCalendar(newValue, this.month);
                this.requestMonthBookings();
            }
        },
        changeCalendar(yearInput, monthInput) {
            const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
            const daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
            const date = new Date(yearInput, monthInput, 1);
            const year = date.getFullYear();
            const month = date.getMonth();
            let days = daysPerMonth[month];

            this.year = year;
            this.month = month;
            this.monthWord = months[month];

            if(month === 1) {  
                if(year % 400 === 0 || year % 4 === 0 && year % 100 !== 0) {
                    days++;
                }
            }
                
            const calendarArray = [[]];
            const startAt = date.getDay() - 1 < 0? 6: date.getDay() - 1;
            let daysCount = 1;
            for(let x = 0; x < 7; x++) {
                if(x === startAt) {
                    calendarArray[0][x] = daysCount;
                    daysCount++;
                } else if(x > startAt) {
                    calendarArray[0][x] = daysCount;
                    daysCount++;
                } else {
                    calendarArray[0][x] = '';
                }
            }

            for(let x = 1; x < 6; x++) {
                if(daysCount >= days) {
                    break;
                }
                calendarArray.push([]);
                for(let y = 0; y < 7; y++) {
                    if(daysCount <= days) {
                        calendarArray[x][y] = daysCount;
                        daysCount++; 
                    } else {
                        calendarArray[x][y] = '';
                    }
                }
            }

            return calendarArray;
        }
    },
    computed: {
        ...mapGetters([
            'bookingStart',
            'bookingEnd',
            'bookings',
            'hotelId'
        ])
    }
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';
    @import '../../../scss/mixins.scss';

    .calendar__container__hotel__info {
        width: 275px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        @include small-phone {
            width: 232px;
        }

        .calendar__options {
            padding: 0 9px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: $input-bg-color;
            height: 47px;

            .calendar__month {
                display: flex;
                align-items: center;

                span {
                    display: block;
                    color: $secondary-color-two;
                    font-family: $primary-font;
                    text-transform: none;
                    text-align: center;
                    font-size: 1rem;
                    font-weight: 400;
                    margin: 0 10px;
                    width: 75px;
                }
            }

            .calendar__year {
                display: flex;
                align-items: center;

                span {
                    font-family: $primary-font;
                    text-transform: none;
                    text-align: center;
                    color: $secondary-color-two;
                    font-size: 1rem;
                    font-weight: 400;
                    margin: 0 10px;
                    width: 55px;
                }
            }

            img {
                cursor: pointer;
            }
        }

        .calendar__date {

            .calendar__days-week {
                padding: 0 10px;
                display: flex;

                span {
                    display: block;
                    width: 39px;
                    text-align: center;
                    margin-top: 15px;
                    margin-bottom: 5px;
                    font-family: $secondary-font;
                    color: $light-gray-text-color;
                    font-weight: 300;
                    font-size: 0.875rem;
                }
            }

            .calendar__days {
                padding: 0 10px;

                ul {
                    list-style: none;
                    margin: 0;
                    padding: 0;
                    display: flex;

                    li {
                        font-family: $primary-font;
                        text-transform: none;
                        text-align: center;
                        margin: 5px 0;
                        width: 39px;
                        color: $gray-text-color;
                        font-weight: 300;
                        font-size: 1rem;
                        border-radius: 30px;
                    }

                    .li-hover {
                        cursor: pointer;
                    }

                    .li-hover:hover {
                        background-color: $input-bg-color;
                    }
                }

                ul:last-child {
                    padding-bottom: 10px;
                }
            }
        }
    }
</style>