<template>
	<div class="min-h-screen bg-gray-50">
		<div class="mx-auto max-w-4xl px-4 py-8">
			<article class="prose prose-lg max-w-none">
				<h1 class="mb-6 text-3xl font-bold text-gray-900">
					股票紀念品是什麼？台灣股東會紀念品完整解析
				</h1>

				<div class="mb-8 grid grid-cols-10 gap-6">
					<div class="col-span-7">
						<p class="text-xl text-gray-700">
							股票紀念品是什麼？本頁完整解析台灣股東會紀念品領取方式、熱門紀念品種類與最新查詢方法，讓你輕鬆掌握
							<span class="tag-block tag-block-primary">高CP值股東福利</span>
							！由
							<span class="tag-block tag-block-special">一股超人</span>
							整理，專為台灣投資人打造的股東會紀念品查詢平台。
						</p>
					</div>
					<div class="col-span-3">
						<img
							src="/images/stock-souvenir-guide/gift-shareholder-concept.png"
							alt="股東獲得紀念品插圖"
							class="h-full w-full rounded-xl object-cover shadow-md"
							loading="lazy"
						/>
					</div>
				</div>

				<section class="mb-12">
					<h2 class="mb-4 text-2xl font-semibold text-gray-800">什麼是股票紀念品？</h2>
					<p class="text-gray-700">
						股票紀念品，又稱「
						<span class="tag-block tag-block-primary">股東會紀念品</span>
						」，是台灣上市櫃公司為感謝股東參與年度股東大會，所提供的實體禮品或紀念性贈品。這些紀念品不僅具有象徵意義，也能提升股東參與意願，增進公司與股東間的互動關係。
					</p>
				</section>

				<section class="mb-12">
					<h2 class="mb-4 text-2xl font-semibold text-gray-800">
						為什麼股票紀念品在台灣特別熱門？
					</h2>
					<p class="text-gray-700">
						在台灣，部分公司發放的股東會紀念品價值，常常超過持有一股股票的成本。因此，許多投資人會以「
						<span class="tag-block tag-block-special">零股</span>
						」方式持有多家公司的股票，只為領取高CP值的紀念品，這也成為台股市場獨特且有趣的現象。這種「
						<span class="tag-block tag-block-special">一股超人</span>
						」的投資方式，讓小資族也能輕鬆參與、收集各家紀念品。
					</p>
				</section>

				<section class="mb-12">
					<h2 class="mb-4 text-2xl font-semibold text-gray-800">常見的股東會紀念品類型</h2>

					<div class="grid grid-cols-10 gap-6">
						<div class="col-span-6">
							<img
								src="/images/stock-souvenir-guide/souvenir-types-flat.png"
								alt="紀念品種類總覽"
								class="mb-4 w-full rounded-xl shadow-md"
								loading="lazy"
							/>
						</div>

						<div class="col-span-4">
							<ul class="list-disc space-y-2 pl-6 text-gray-700">
								<li
									v-for="category in Object.keys(GIFT_CATEGORY_MAP)"
									:key="category"
								>
									<NuxtLink
										:to="`/companies?category=${encodeURIComponent(category)}`"
										class="text-primary-600 hover:underline"
									>
										{{ category }}
									</NuxtLink>
								</li>
							</ul>
						</div>
					</div>
				</section>

				<section class="mb-12">
					<h2 class="mb-4 text-2xl font-semibold text-gray-800">如何領取股東會紀念品？</h2>

					<div class="info-block">
						<div class="info-block-title">重要提醒</div>
						<div class="info-block-content">
							最後買進日通常為股東會前62日，建議提前規劃並查詢各公司公告。
						</div>
					</div>

					<ol class="list-decimal space-y-4 pl-6 text-gray-700">
						<li>
							<strong>持有資格</strong>
							：需在「
							<span class="tag-block tag-block-primary">最後買進日</span>
							」前持有該公司股票。最後買進日通常為股東會前62日，建議查詢各公司公告。
						</li>
						<li>
							<strong>零股領取</strong>
							：多數公司不限持股數，
							<span class="tag-block tag-block-special">一股即可領取</span>
							；部分公司有最低持股門檻或特殊規定，請詳閱公告。
						</li>
						<li>
							<strong>領取方式</strong>
							：
							<ul class="mt-2 list-disc space-y-2 pl-6">
								<li>親自出席股東會</li>
								<li>以電子方式行使表決權</li>
								<li>持股東會通知書至指定地點領取</li>
								<li>部分公司可於APP、線上兌換</li>
							</ul>
						</li>
						<li>
							<strong>注意事項</strong>
							：
							<ul class="mt-2 list-disc space-y-2 pl-6">
								<li>零股股東領取方式、資格各公司不同</li>
								<li>領取時須攜帶身分證、電子投票截圖或相關證明文件</li>
								<li>部分公司需親自領取或委託業者代領</li>
							</ul>
						</li>
					</ol>
				</section>

				<section class="mb-12">
					<h2 class="mb-4 text-2xl font-semibold text-gray-800">股東會紀念品攻略與小技巧</h2>
					<ul class="list-disc space-y-2 pl-6 text-gray-700">
						<li>
							<strong>善用零股投資</strong>
							：「
							<span class="tag-block tag-block-special">一股超人</span>
							」小資族可用極低成本參與多家公司，領取多樣紀念品。
						</li>
						<li>
							<strong>提前規劃買進時點</strong>
							：掌握每家公司「
							<span class="tag-block tag-block-primary">最後買進日</span>
							」，避免錯過領取資格。
						</li>
						<li>
							<strong>查詢熱門紀念品公司</strong>
							：如
							<NuxtLink
								:to="`/companies?search=${encodeURIComponent('大魯閣')}`"
								class="text-primary-600 hover:underline"
							>
								大魯閣
							</NuxtLink>
							、
							<NuxtLink
								:to="`/companies?search=${encodeURIComponent('聯電')}`"
								class="text-primary-600 hover:underline"
							>
								聯電
							</NuxtLink>
							、
							<NuxtLink
								:to="`/companies?search=${encodeURIComponent('王品')}`"
								class="text-primary-600 hover:underline"
							>
								王品
							</NuxtLink>
							、
							<NuxtLink
								:to="`/companies?search=${encodeURIComponent('長榮')}`"
								class="text-primary-600 hover:underline"
							>
								長榮
							</NuxtLink>
							、
							<NuxtLink
								:to="`/companies?search=${encodeURIComponent('中鋼')}`"
								class="text-primary-600 hover:underline"
							>
								中鋼
							</NuxtLink>
							等，近年紀念品CP值高且具話題性。
						</li>
						<li>
							<strong>關注公告與規則</strong>
							：每年紀念品內容、領取方式、門檻可能調整，需密切留意公司公告。
						</li>
						<li>
							<strong>電子投票更方便</strong>
							：多數公司接受電子投票即具備領取資格，省去親自出席的麻煩。
						</li>
					</ul>
				</section>

				<section class="mb-12">
					<h2 class="mb-4 text-2xl font-semibold text-gray-800">投資人須知與常見問題</h2>
					<div class="info-block">
						<div class="info-block-title">重要提醒</div>
						<div class="info-block-content">
							並非所有公司都會發放紀念品，發放與否及內容以公司公告為準。零股股東請特別留意各公司規定。
						</div>
					</div>
					<ul class="list-disc space-y-2 pl-6 text-gray-700">
						<li>並非所有公司都會發放紀念品，發放與否及內容以公司公告為準。</li>
						<li>零股股東領取方式及資格，請特別留意各公司規定。</li>
						<li>
							記得查詢最新的股東會紀念品清單與
							<span class="tag-block tag-block-primary">最後買進日</span>
							，避免錯過領取資格。
						</li>
						<li>有些公司會限制「未滿一定股數」的股東僅能以電子投票或親自出席領取紀念品。</li>
					</ul>
				</section>
			</article>
		</div>
	</div>
</template>

<script setup>
	import GIFT_CATEGORY_MAP from '~/config/category';

	useHead({
		title: '股票紀念品是什麼？台灣股東會紀念品完整解析',
		meta: [
			{
				name: 'description',
				content:
					'完整解析台灣股東會紀念品領取方式、熱門紀念品種類與最新查詢方法。了解股票紀念品、股東會紀念品相關資訊，掌握高CP值股東福利！由一股超人整理，專為台灣投資人打造的股東會紀念品查詢平台。',
			},
			{
				name: 'keywords',
				content: '股票紀念品, 股東會紀念品, 台灣, 查詢, 零股, 股東福利, 紀念品領取, 一股超人',
			},
		],
	});

	useJsonld(() => ({
		'@context': 'https://schema.org',
		'@type': 'FAQPage',
		mainEntity: [
			{
				'@type': 'Question',
				name: '什麼是股票紀念品？',
				acceptedAnswer: {
					'@type': 'Answer',
					text: '股票紀念品是上市櫃公司為感謝股東參與股東會所發放的贈品，例如商品卡、餐具、保健品等。',
				},
			},
			{
				'@type': 'Question',
				name: '要怎麼領股票紀念品？',
				acceptedAnswer: {
					'@type': 'Answer',
					text: '需在股東會前的最後過戶日前持有股票，並依公司規定完成出席或表決，即可領取紀念品。',
				},
			},
			{
				'@type': 'Question',
				name: '持有一股就可以領股票紀念品嗎？',
				acceptedAnswer: {
					'@type': 'Answer',
					text: '多數公司只要持有一股即可領取，但有些公司可能需達最低股數或實際出席，請依公告為主。',
				},
			},
			{
				'@type': 'Question',
				name: '有哪些熱門股東會紀念品？',
				acceptedAnswer: {
					'@type': 'Answer',
					text: '常見的紀念品包括7-11商品卡、咖啡券、碗盤組、毛巾、保溫瓶、面膜、益生菌等生活用品。',
				},
			},
		],
	}));
</script>
