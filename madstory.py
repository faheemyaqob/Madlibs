import streamlit as st
import random

# Page setup
st.set_page_config(page_title="Mad Libs Fun", page_icon="🧠")

# Sidebar instructions
with st.sidebar:
    st.title("📘 How to Play")
    st.markdown("""
    1. Fill in the blanks  
    2. Click **Generate Story**  
    3. Get a surprise story each time! 🎲  
    4. Try new words and hit "Generate" again

    Let's get silly! 😜
    """)

# Main title
st.title("🎉 Quick & Random Mad Libs")
st.markdown("Just 5 words = instant nonsense fun! 🤪")

# Inputs
st.markdown("### ✍️ Your Words")
animal = st.text_input("🐾 Name an animal")
place = st.text_input("📍 Name a place")
verb_past = st.text_input("🏃 Verb (past tense)")
food = st.text_input("🍕 Favorite food")
adjective = st.text_input("💫 Adjective")

# Story templates
templates = [
    "One day, a {animal} went to the {place}. It {verb_past} until it found some {food}. It was a {adjective} time!",
    "At the {place}, a {animal} suddenly {verb_past} into a plate of {food}. Everyone called it the most {adjective} moment ever.",
    "Once upon a time, a {adjective} {animal} visited the {place}. It couldn't stop {verb_past} after smelling {food}.",
    "The {animal} was feeling {adjective}, so it traveled to the {place} and {verb_past} with a bucket of {food}.",
    "While exploring the {place}, a {animal} {verb_past} and tripped over {food}. How {adjective}!"
]

# Generate story
if st.button("🎲 Generate Story!"):
    if all([animal, place, verb_past, food, adjective]):
        story_template = random.choice(templates)
        story = story_template.format(
            animal=animal,
            place=place,
            verb_past=verb_past,
            food=food,
            adjective=adjective
        )

        # Styled output
        st.markdown(
            f"""
            <div style='background-color:#fff5e6;padding:20px;border-radius:10px'>
                <h3 style='color:#6a5acd;'>📝 Here's Your Mad Lib:</h3>
                <p style='font-size:18px;'>{story} 🎉</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Please fill in all 5 blanks to create a story.")