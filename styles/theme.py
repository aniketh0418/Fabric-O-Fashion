import streamlit as st

# Enhanced color palette with opacity variations
COLORS = {
    # Primary colors
    'primary': {
        'main': '#7C3AED',  # Purple
        'light': '#9F67FF',
        'dark': '#5B21B6',
        'transparent': 'rgba(124, 58, 237, 0.1)',
    },
    # Secondary colors
    'secondary': {
        'main': '#4F46E5',  # Indigo
        'light': '#818CF8',
        'dark': '#3730A3',
        'transparent': 'rgba(79, 70, 229, 0.1)',
    },
    # Accent colors
    'accent': {
        'main': '#10B981',  # Emerald
        'light': '#34D399',
        'dark': '#059669',
        'transparent': 'rgba(16, 185, 129, 0.1)',
    },
    # Dark theme specific colors
    'dark': {
        'background': '#0F172A',  # Darker blue-gray
        'surface': '#1E293B',     # Dark blue-gray
        'card': '#334155',        # Medium blue-gray
        'border': '#475569',      # Light blue-gray
    },
    # Text colors
    'text': {
        'primary': '#F8FAFC',     # Almost white
        'secondary': '#CBD5E1',   # Light gray
        'muted': '#64748B',       # Muted blue-gray
        'link': '#38BDF8',        # Sky blue
    },
    # Status colors
    'status': {
        'success': '#10B981',     # Green
        'warning': '#F59E0B',     # Amber
        'error': '#EF4444',       # Red
        'info': '#0EA5E9',        # Sky blue
    }
}

# Enhanced typography system
TYPOGRAPHY = {
    'font_family': {
        'primary': '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        'code': '"JetBrains Mono", monospace',
    },
    'font_sizes': {
        'xs': '0.75rem',
        'sm': '0.875rem',
        'base': '1rem',
        'lg': '1.125rem',
        'xl': '1.25rem',
        '2xl': '1.5rem',
        '3xl': '1.875rem',
        '4xl': '2.25rem',
    },
    'font_weights': {
        'normal': '400',
        'medium': '500',
        'semibold': '600',
        'bold': '700',
    },
    'line_heights': {
        'tight': '1.25',
        'normal': '1.5',
        'relaxed': '1.75',
    }
}

# Enhanced spacing system
SPACING = {
    '0': '0',
    'px': '1px',
    '0.5': '0.125rem',
    '1': '0.25rem',
    '2': '0.5rem',
    '3': '0.75rem',
    '4': '1rem',
    '5': '1.25rem',
    '6': '1.5rem',
    '8': '2rem',
    '10': '2.5rem',
    '12': '3rem',
    '16': '4rem',
}

# Animation configurations
ANIMATIONS = {
    'transition_time': {
        'fast': '150ms',
        'normal': '300ms',
        'slow': '500ms',
    },
    'transition_curve': {
        'default': 'cubic-bezier(0.4, 0, 0.2, 1)',
        'in': 'cubic-bezier(0.4, 0, 1, 1)',
        'out': 'cubic-bezier(0, 0, 0.2, 1)',
        'in_out': 'cubic-bezier(0.4, 0, 0.2, 1)',
    }
}

# Shadows for depth
SHADOWS = {
    'sm': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
    'md': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
    'lg': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
    'xl': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
}

def apply_theme():
    """Apply enhanced custom theme to Streamlit app"""
    
    # Custom CSS with advanced styling
    st.markdown(
        f"""
        <style>
            /* Base styles and CSS reset */
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            /* Main app container */
            .stApp {{
                background-color: {COLORS['dark']['background']};
                color: {COLORS['text']['primary']};
                font-family: {TYPOGRAPHY['font_family']['primary']};
                transition: all {ANIMATIONS['transition_time']['normal']} {ANIMATIONS['transition_curve']['default']};
            }}
            
            /* Typography enhancements */
            h1, h2, h3, h4, h5, h6 {{
                color: {COLORS['text']['primary']};
                font-family: {TYPOGRAPHY['font_family']['primary']};
                font-weight: {TYPOGRAPHY['font_weights']['bold']};
                line-height: {TYPOGRAPHY['line_heights']['tight']};
                letter-spacing: -0.025em;
            }}
            
            /* Sidebar styling */
            .css-1d391kg {{
                background-color: {COLORS['dark']['surface']};
                border-right: 1px solid {COLORS['dark']['border']};
            }}
            
            /* Card components */
            .stCard {{
                background-color: {COLORS['dark']['card']};
                border: 1px solid {COLORS['dark']['border']};
                border-radius: 0.75rem;
                padding: {SPACING['4']};
                box-shadow: {SHADOWS['md']};
                transition: transform {ANIMATIONS['transition_time']['normal']} {ANIMATIONS['transition_curve']['default']},
                            box-shadow {ANIMATIONS['transition_time']['normal']} {ANIMATIONS['transition_curve']['default']};
            }}
            
            .stCard:hover {{
                transform: translateY(-2px);
                box-shadow: {SHADOWS['lg']};
            }}
            
            /* Button styling */
            .stButton>button {{
                background-color: {COLORS['primary']['main']};
                color: {COLORS['text']['primary']};
                border: none;
                border-radius: 0.5rem;
                padding: {SPACING['2']} {SPACING['4']};
                font-weight: {TYPOGRAPHY['font_weights']['medium']};
                transition: all {ANIMATIONS['transition_time']['fast']} {ANIMATIONS['transition_curve']['default']};
                box-shadow: {SHADOWS['sm']};
            }}
            
            .stButton>button:hover {{
                background-color: {COLORS['primary']['dark']};
                box-shadow: {SHADOWS['md']};
                transform: translateY(-1px);
            }}
            
            /* Input fields */
            .stTextInput>div>div>input {{
                background-color: {COLORS['dark']['surface']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['dark']['border']};
                border-radius: 0.5rem;
                padding: {SPACING['3']};
                transition: all {ANIMATIONS['transition_time']['fast']} {ANIMATIONS['transition_curve']['default']};
            }}
            
            .stTextInput>div>div>input:focus {{
                border-color: {COLORS['primary']['main']};
                box-shadow: 0 0 0 2px {COLORS['primary']['transparent']};
            }}
            
            /* Select boxes */
            .stSelectbox>div>div {{
                background-color: {COLORS['dark']['surface']};
                border: 1px solid {COLORS['dark']['border']};
                border-radius: 0.5rem;
            }}
            
            /* Slider styling */
            .stSlider>div>div {{
                background-color: {COLORS['dark']['surface']};
            }}
            
            .stSlider>div>div>div>div {{
                background-color: {COLORS['primary']['main']};
            }}
            
            /* Progress bars */
            .stProgress>div>div>div>div {{
                background-color: {COLORS['primary']['main']};
            }}
            
            /* Tables */
            .stTable {{
                background-color: {COLORS['dark']['surface']};
                border: 1px solid {COLORS['dark']['border']};
                border-radius: 0.75rem;
                overflow: hidden;
            }}
            
            .stTable thead tr th {{
                background-color: {COLORS['dark']['card']};
                color: {COLORS['text']['primary']};
                padding: {SPACING['3']};
                font-weight: {TYPOGRAPHY['font_weights']['semibold']};
            }}
            
            .stTable tbody tr td {{
                padding: {SPACING['3']};
                border-top: 1px solid {COLORS['dark']['border']};
            }}
            
            /* Code blocks */
            .stCode {{
                font-family: {TYPOGRAPHY['font_family']['code']};
                background-color: {COLORS['dark']['surface']};
                border: 1px solid {COLORS['dark']['border']};
                border-radius: 0.5rem;
            }}
            
            /* Tooltips */
            .stTooltip {{
                background-color: {COLORS['dark']['card']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['dark']['border']};
                border-radius: 0.5rem;
                padding: {SPACING['2']} {SPACING['3']};
                box-shadow: {SHADOWS['lg']};
            }}
            
            /* Scrollbar styling */
            ::-webkit-scrollbar {{
                width: 8px;
                height: 8px;
            }}
            
            ::-webkit-scrollbar-track {{
                background: {COLORS['dark']['surface']};
            }}
            
            ::-webkit-scrollbar-thumb {{
                background: {COLORS['dark']['border']};
                border-radius: 4px;
            }}
            
            ::-webkit-scrollbar-thumb:hover {{
                background: {COLORS['text']['muted']};
            }}
            
            /* Charts and plots */
            .js-plotly-plot {{
                background-color: {COLORS['dark']['surface']};
                border: 1px solid {COLORS['dark']['border']};
                border-radius: 0.75rem;
                padding: {SPACING['4']};
                box-shadow: {SHADOWS['md']};
            }}
            
            /* Animations for page transitions */
            .main .stPage {{
                animation: fadeIn {ANIMATIONS['transition_time']['normal']} {ANIMATIONS['transition_curve']['out']};
            }}
            
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(10px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            
            /* Status indicators */
            .status-success {{
                color: {COLORS['status']['success']};
            }}
            
            .status-warning {{
                color: {COLORS['status']['warning']};
            }}
            
            .status-error {{
                color: {COLORS['status']['error']};
            }}
            
            .status-info {{
                color: {COLORS['status']['info']};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

def apply_card_style():
    """Helper function to apply card styling to a container"""
    return """
        <div class="stCard">
            {content}
        </div>
    """

def apply_status_style(status_type):
    """Helper function to apply status styling"""
    return f'<span class="status-{status_type}">'