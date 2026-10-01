import streamlit as st

# -----------------------------
# LegalEase - Main Application
# -----------------------------

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)

# ---------- Header ----------
st.title("⚖️ LegalEase")
st.subheader("Your Simple Legal Assistance Companion")

st.info(
    "LegalEase provides general legal information and guidance. "
    "It is not a substitute for advice from a qualified lawyer."
)

# ---------- Sidebar ----------
st.sidebar.title("LegalEase Menu")

option = st.sidebar.selectbox(
    "Choose an option",
    [
        "Home",
        "Legal Information",
        "Document Assistant",
        "Ask LegalEase",
        "About"
    ]
)

# ---------- Home ----------
if option == "Home":
    st.header("Welcome to LegalEase")

    st.write(
        """
        LegalEase is designed to make basic legal information easier to
        understand and access.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📚 Legal Information")
        st.write("Learn about common legal topics in simple language.")

    with col2:
        st.markdown("### 📄 Document Assistant")
        st.write("Get help understanding common legal documents.")

    with col3:
        st.markdown("### 💬 Ask LegalEase")
        st.write("Ask questions and receive general legal information.")

# ---------- Legal Information ----------
elif option == "Legal Information":
    st.header("📚 Legal Information")

    topic = st.selectbox(
        "Select a topic",
        [
            "Consumer Rights",
            "Cyber Crime",
            "Employment",
            "Property",
            "Family Law",
            "Criminal Law",
            "Contracts"
        ]
    )

    legal_info = {
        "Consumer Rights":
            "Consumers generally have rights relating to product quality, "
            "services, refunds, and unfair trade practices.",

        "Cyber Crime":
            "Cyber crimes can include online fraud, identity theft, "
            "unauthorized access, and other offences involving digital systems.",

        "Employment":
            "Employment law can cover wages, working conditions, contracts, "
            "leave, termination, and workplace rights.",

        "Property":
            "Property law may involve ownership, transfer, rental agreements, "
            "inheritance, and disputes over property.",

        "Family Law":
            "Family law can cover marriage, divorce, maintenance, custody, "
            "adoption, and related matters.",

        "Criminal Law":
            "Criminal law deals with offences and the legal procedures "
            "associated with investigation and prosecution.",

        "Contracts":
            "A contract generally establishes legally relevant rights and "
            "obligations between parties."
    }

    st.write(legal_info[topic])

# ---------- Document Assistant ----------
elif option == "Document Assistant":
    st.header("📄 Document Assistant")

    document_type = st.selectbox(
        "Choose document type",
        [
            "Rental Agreement",
            "Employment Agreement",
            "Sale Agreement",
            "Non-Disclosure Agreement",
            "Other"
        ]
    )

    document_text = st.text_area(
        "Paste your document here",
        height=250
    )

    if st.button("Analyze Document"):
        if document_text.strip():
            st.success("Document received.")

            st.markdown("### Basic Analysis")
            st.write(
                f"Document type selected: **{document_type}**"
            )

            st.write(
                "LegalEase can help identify important sections, "
                "key dates, obligations, and potentially unclear clauses."
            )

            st.warning(
                "This is a general informational analysis and should not "
                "be treated as legal advice."
            )
        else:
            st.error("Please paste a document before analyzing it.")

# ---------- Ask LegalEase ----------
elif option == "Ask LegalEase":
    st.header("💬 Ask LegalEase")

    question = st.text_area(
        "Enter your legal question:",
        placeholder="Example: What should I check before signing a rental agreement?"
    )

    if st.button("Get Information"):
        if question.strip():
            st.write("### LegalEase Response")

            # Simple demo response.
            # Replace this section with an AI/API call later.
            st.write(
                """
                Based on your question, you should first identify the
                relevant area of law and check the applicable laws and
                official government resources.

                For an actual legal dispute or important legal decision,
                consider consulting a qualified lawyer.
                """
            )

            st.caption(
                "LegalEase provides general information and does not "
                "create an attorney-client relationship."
            )
        else:
            st.error("Please enter a question.")

# ---------- About ----------
elif option == "About":
    st.header("ℹ️ About LegalEase")

    st.write(
        """
        **LegalEase** is a project designed to improve access to
        understandable legal information.

        ### Project Goals
        - Simplify complex legal concepts
        - Help users find relevant information
        - Assist users in understanding documents
        - Provide an easy-to-use legal information interface
        """
    )

    st.warning(
        "LegalEase is an educational project. It should not be used as "
        "a replacement for professional legal advice."
    )

# ---------- Footer ----------
st.markdown("---")
st.caption("© 2026 LegalEase | Educational Project")
