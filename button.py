from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


reply_builder = ReplyKeyboardBuilder()

reply_builder.button(text="Купить билет")
reply_builder.button(text="Действующие билеты")
reply_builder.button(text="Подписка СБП")
reply_builder.button(text="Ещё...")

reply_builder.adjust(2)

reply_kb = reply_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=False
)

inline_builder_buy = InlineKeyboardBuilder()
inline_builder_sbp = InlineKeyboardBuilder()
inline_builder_more = InlineKeyboardBuilder()

# Клавиатура купить билет
inline_builder_buy.button(text="📷 Сканер QR", callback_data="qr_scanner_not_ready")
inline_builder_buy.button(text="🔢 Ввести код", callback_data="enter_code_not_ready")

inline_builder_buy.adjust(1, 1)

inline_kb_buy = inline_builder_buy.as_markup()

# Клавиатура СБП
inline_builder_sbp.button(text="➕ Добавить подписку СБП", callback_data="sbp_add_not_ready")

inline_kb_sbp = inline_builder_sbp.as_markup()

# Клавиатура "Ещё..."
inline_builder_more.button(text="👤 Мой ID", callback_data="my_id_not_ready")
inline_builder_more.button(text="📄 Правила", callback_data="rules_not_ready")
inline_builder_more.button(text="🚌 Online маршрут", callback_data="online_route_not_ready")
inline_builder_more.button(text="📧 E-mail для чеков", callback_data="email_receipts_not_ready")
inline_builder_more.button(text="🔄 Запросить возврат", callback_data="refund_not_ready")
inline_builder_more.button(text="🆘 Обращение в поддержку", callback_data="support_not_ready")

inline_builder_more.adjust(1, 1, 1, 1, 1, 1)

inline_kb_more = inline_builder_more.as_markup()
