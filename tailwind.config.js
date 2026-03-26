module.exports = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        primary: "#7f1d1d",
                        "primary-hover": "#991b1b",
                        "background-dark": "#050507",
                        "surface-dark": "#0a0a0c",
                                                "text-dark": "#ffffff",
                        gray: {
                            300: "#f9fafb",
                            400: "#f3f4f6",
                            500: "#e5e7eb",
                            600: "#d1d5db",
                        }
                    },
                    fontFamily: {
                        display: ["Inter", "sans-serif"],
                        body: ["Inter", "sans-serif"],
                        poppins: ["Poppins", "sans-serif"],
                    },
                    borderRadius: {
                        DEFAULT: "0.5rem",
                    },
                },
            },
        };
module.exports.content = ['./*.html'];
module.exports.plugins = [require('@tailwindcss/typography'), require('@tailwindcss/forms'), require('@tailwindcss/container-queries')];
