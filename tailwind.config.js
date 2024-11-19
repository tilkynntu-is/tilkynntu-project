/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./Project/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        quicksand: ['Quicksand', 'sans-serif'],
      },
      keyframes: {
        fadeUp: {
          '0%': { opacity: '0', transform: 'translateY(0px)' },
          '100%': { opacity: '1', transform: 'translateY(-20px)' },
        },
      },
      animation: {
        fadeUp: 'fadeUp 0.5s ease-out forwards',
      },
    },
  },
  plugins: [],
};
